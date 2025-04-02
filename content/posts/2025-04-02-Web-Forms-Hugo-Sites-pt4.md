---
title: "Web Forms Hugo Sites - Part 4"
date: 2025-04-02T16:13:50-04:00
draft: false
---

Previous posts:

- [Web Forms On Hugo Sites - Part 1]({{< relref "2025-03-18-Web-Forms-Hugo-Sites-pt1" >}})
- [Web Forms On Hugo Sites - Part 2]({{< relref "2025-03-19-Web-Forms-Hugo-Sites-pt2" >}})
- [Web Forms On Hugo Sites - Part 3]({{< relref "2025-04-01-Web-Forms-Hugo-Sites-pt3" >}})

---

The saga of the web forms continues.

Last, we left our intrepid project and were dealing with an issue with the _self-signed_ certificate for our database. After poking around TLS, one of my brilliant friends sent me the following links:

- **For postgres** - https://github.com/porsager/postgres#ssl
- **For pg** - https://node-postgres.com/features/ssl#self-signed-cert

To use the `pg` library we would use the second one. The issue is that I only have the self-signed certificate.

---

Setting the `NODE_TLS_REJECT_UNAUTHORIZED` environment variable to `'0'` works, but there was still hope for a better solution. My heart fell when I got the support ticket response from Digital Ocean.

Here are some relevant parts from the email

> Basically, other than MongoDB, our managed databases use self-signed certificates. This is why you are seeing this error, you can either use env variable NODE_TLS_REJECT_UNAUTHORIZED=0 to ignore the error or you can deploy the database on a droplet and configure the SSL certificate from any certificate authority.
>
> I will recommend going through the below documents that covers this issue:  
> [https://stackoverflow.com/questions/45088006/nodejs-error-self-signed-certificate-in-certificate-chain](https://stackoverflow.com/questions/45088006/nodejs-error-self-signed-certificate-in-certificate-chain)  
> [https://www.digitalocean.com/community/questions/can-t-connect-via-nodejs-error-self-signed-certificate-in-certificate-chain](https://www.digitalocean.com/community/questions/can-t-connect-via-nodejs-error-self-signed-certificate-in-certificate-chain)

Arg.

This solution strikes me as not a good plan for production-level code. Everywhere I see mention of NODE_TLS_REJECT_UNAUTHORIZED, there is mention of how NOT TO USE IT IN PRODUCTION. Oops, well, it looks like that is the solution to using pg. I've pushed back and asked for more clarification from the support team at Digital Ocean, but for now, here is a safer way to use the env variable in the code.

```javascript
export async function main(args) {
  let name = "star-gazer";
  let greeting = "Hello there, " + name + "!";

  let connectionString = process.env.CONNECTION_STRING;

  const client = new Client({
    connectionString: connectionString,
    ssl: {
      rejectUnauthorized: false,
      ca: fs.readFileSync("./certs/ca-certificate.crt"),
    },
  });

  process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = "0";
  try {
    await client.connect();
  } catch (error) {
    return {
      body: "There was an error connecting to the database: " + error.message,
    };
  }

  const res = await client.query("SELECT * FROM test_table;");
  await client.end();

  delete process.env["NODE_TLS_REJECT_UNAUTHORIZED"];

  return { body: greeting, response: res.rows };
}
```

Putting it in a try/catch/finally block might be even safer to ensure the environment variable is unset. Truthfully, the nature of the serverless function is that the environment is constructed and removed for the function's use, so it probably isn't necessary to do it in JavaScript here instead of setting it in the project.yml file. The benefit of doing it here vs. there is that if there are additional functions, only the ones that need it will have the exception set.

## Conclusion

This still isn't a strong solution to this problem. Although there are a couple out there, I doubt how successful this project will be and whether I want to pay for another form of backend solution.

But I've started it, and like my friend Mike always says, I struggle to give up, even if I'm slow.

Next up: creating the functions to insert data into the database. Working on limits for daily submissions to prevent spamming. Adding additional security. Things like that.
