---
title: "Web Forms Hugo Sites - Part 3"
date: 2025-04-01T13:26:16-04:00
draft: false
tags: ["programming"]
---

Previous posts:

- [Web Forms On Hugo Sites - Part 1]({{< relref "2025-03-18-Web-Forms-Hugo-Sites-pt1" >}})
- [Web Forms On Hugo Sites - Part 2]({{< relref "2025-03-19-Web-Forms-Hugo-Sites-pt2" >}})

The next step in the process is writing the serverless function on the Digital Ocean App Platform to connect to the database. _Warning:_ this post will not be a happy one. I'm in the middle of figuring out the best way to do this, but I've learned some things, and so I decided to share them.

## Choosing a Postgres Library

When you got https://www.npmjs.com and look for a package to connect to Postgres, there are two main options:

- https://www.npmjs.com/package/postgres
- https://www.npmjs.com/package/pg

For most of the work I've been doing I've been using the Postgres package. It was used in examples found online so that was what I was using. Upon looking at their pages, I found several interesting things, node-postgres (pg) has about 8 million weekly downloads. Postgres has only about 600 thousand. Node-postgres also has some very recent code contributions, while Postgres seems to have must less frequent updates.

This means changing my code around a bit to use Node-Postgres instead of the Postgres library. Shouldn't be that hard.

The source for the function using node-postgres looks something like this:

```javascript
import pg from "pg";
const { Client } = pg;

export async function main(args) {
  let name = "star-gazer";
  let greeting = "Hello there, " + name + "!";

  // Trying to connect to the database
  let connectionString = process.env.CONNECTION_STRING;

  try {
    const client = new Client({
      connectionString,
    });
  } catch (error) {
    return {
      body: "There was an error creating the client: " + error.message,
    };
  }

  try {
    await client.connect();
  } catch (error) {
    return {
      body: "There was an error connecting to the database: " + error.message,
    };
  }

  const res = await client.query("SELECT * FROM test_table;");
  await client.end();

  return { body: greeting, response: res.rows };
}
```

If this looks a little wonky its because I've copied it from the massive amount of attempts I've taken to get this working. The issue with the above is that while my database server is on an internal cluster and is only available to machines with a specific VPN, and even has a CA certificate installed. The signing agent for the certificate is Digital Ocean. This is a **self-signed certificate** and the node-postgres library is concerned about the security of that certificate.

**Self-signed certificates** are bad, and it's good that Postgres attempts to prevent users from using them. Unfortunately, I'm unable to find a simple way to tell the library that I know what I'm doing and trust this connection.

## Choices

This conundrum leads to a couple of options for solving this problem. None of them are great.

### Option 1: Stick with the Postgres Library

I have confirmed, with some testing, that the Postgres library does indeed seem to ignore the self-signed certification, so using that library would dodge this issue.

The downside of this approach is that I'm using a less well-maintained library. While that doesn't impact me at this moment, maybe there is a feature that I will need from node-postgres in the future and won't have access to because of my library choice. Also, what if there is a security vulnerability in the `postgres` library?

### Option 2: Accept TLS Unauthorized

You can set a setting at the environmental level to tell the node to accept self-signed certifications.

```sh
> export NODE_TLS_REJECT_UNAUTHORIZED='0'
```

This one command, which can probably be set in the package environments variables section (though I haven't tried that yet), will tell Node's library to stop worrying about unauthorized TLS issues like self-signed certificates.

This isn't good for all sorts of reasons. The prominent one is that I want to let this one connection go through without checking just the self-signed nature of the certificate. I don't want to allow other unsecured connections. This environment variable will allow all connections to be insecure.

In case you set the variable to play with it, I recommend removing it as soon as you are done:

```sh
> unset NODE_TLS_REJECT_UNAUTHORIZED
```

### Option 3: Provide the correct SecureContextOptions

_I haven't gotten this option to work, but if I can figure it out, it's probably the best one._

The connection options for creating the client with `node-postgres` allow you to pass in the following options:

```typescript
export class Client extends ClientBase {
  user?: string | undefined;
  database?: string | undefined;
  port: number;
  host: string;
  password?: string | undefined;
  ssl: boolean;

  constructor(config?: string | ClientConfig);

  end(): Promise<void>;
  end(callback: (err: Error) => void): void;
}
```

This is in the `index.d.ts` file for `pg` Client class. If you search for `ssl` in the file, you will see that the boolean here is a mask:

```javascript
export interface ClientConfig {
	...
	ssl?: boolean | ConnectionOptions | undefined;
    ...
}
```

Investigating the `ConnectionOptions`, `tls.d.ts` defines the interface as:

```typescript
interface ConnectionOptions extends SecureContextOptions, CommonConnectionOptions { ... }
```

`SecureContextOptions` has the property for ca?:

```typescript
        /**
         * Optionally override the trusted CA certificates. The default is to trust
         * the well-known CAs curated by Mozilla. Mozilla's CAs are completely
         * replaced when CAs are explicitly specified using this option.
         */
        ca?: string | Buffer | Array<string | Buffer> | undefined;
```

This is how you can pass in the certificate by using something like:

```javascript
const client = new Client({
  connectionString: connectionString,
  ssl: {
    ca: fs.readFileSync("./certs/ca-cert.crt"),
  },
});
```

The problem is that even if you include the CRT in this way, because it is self-signed, you still end up with a connection error.

This solution still doesn't work. There is no obvious way to obtain a commercial certificate for both your Database server and include in your function.

## Conclusion

I've submitted a support ticket to Digital Ocean to see if there is any direct guidance on the most correct way to do this connection.

In the mean time, the code that I'm going to write after the connection is made should be relatively similar regardless of which Postgres Library used. The next step is parse the arguments sent to the function, really defining the pattern, and inserting them into the database. For now, I'm just going to use the Postgres Library while I wait for a better solution from Digital Ocean.
