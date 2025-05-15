---
title: "Web Forms Hugo Sites - Part 5"
date: 2025-04-03T16:58:22-04:00
draft: false
tags: ["programming"]
---

This is the fifth post about putting dynamic forms on a static [Hugo](https://gohugo.io) site. Please see the previous steps to understand where we are:

- [Web Forms On Hugo Sites - Part 1]({{< relref "2025-03-18-Web-Forms-Hugo-Sites-pt1" >}})
- [Web Forms On Hugo Sites - Part 2]({{< relref "2025-03-19-Web-Forms-Hugo-Sites-pt2" >}})
- [Web Forms On Hugo Sites - Part 3]({{< relref "2025-04-01-Web-Forms-Hugo-Sites-pt3" >}})
- [Web Forms On Hugo Sites - Part 4]({{< relref "2025-04-02-Web-Forms-Hugo-Sites-pt4" >}})

Now it is time for SQL and input!

## Talking about input

The plan for input is something like the following. The body of the post request should look like this:

```json
{
  "formId": "b863745d-53a7-4282-a286-fbd8388ba001",
  "data": [
    {
      "question": "This is a question from a request 1",
      "answer": "This is answer 1"
    },
    {
      "question": "This is question 2",
      "answer": "This is answer 2"
    }
  ]
}
```

This includes two top-level parameters:

- **formId**: allows us to use this input with multiple different forms.
- **data**: is a list of objects containing a question and answer.

The data will be entered into the rows discussed in [[Web Forms On Hugo Sites - Part 2]].

## Handling the input in node

The current approach makes it easy to send in bad data. We will be doing things to protect for that later, but starting with good practices, break out the data input processing to a function:

```javascript
function processArgs(args) {
  if (!args || !args.formId || !args.data) {
    throw new Error("Invalid arguments: formId and data are required");
  }

  const formId = args.formId;
  const submissionId = crypto.randomUUID();
  const dataArray = args.data;

  return {
    formId: formId,
    submissionId: submissionId,
    data: dataArray,
  };
}
```

In the future, this could be a place where go through and check the validity of the data array, but for now, it's just passed through.

## Generate Insert SQL

Next up is the code to generate the SQL used to insert the data into the database. It's pretty easy to read:

```javascript
function getInsertSql(data) {
  const now = new Date();
  const nowString = now.toISOString();
  const formId = data.formId;
  const submissionId = data.submissionId;

  const allStrings = data.data.map((item) => {
    return `('${nowString}', '${formId}', '${submissionId}', '${item.question}', '${item.answer}'),`;
  });
  const dataString = allStrings.join("").slice(0, -1);

  const sql = `INSERT INTO form_data (date_added, form_id, submission_id, question, answer) VALUES ${dataString};`;

  return sql;
}
```

This creates a long SQL statement like:

```sql
INSERT INTO form_data (date_added, form_id, submission_id, question, answer)
VALUES
 (isoString, formID, submission_id, question1, answer1),
 (isoString, formID, submission_id, question2, answer2),
 (isoString, formID, submission_id, question3, answer3)
 ...
```

## Putting it together

Now the arguments are parsed, and SQL is ready, we have to go through the process of writing it to the database:

```javascript
export async function main(args) {
  let name = "star-gazer";
  let greeting = "Hello there, " + name + "!";

  let connectionString = process.env.CONNECTION_STRING;

  const data = processArgs(args);
  const insertSql = getInsertSql(data);

  const rowCount = data.data.length;

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

  const res = await client.query(insertSql);
  await client.end();

  delete process.env["NODE_TLS_REJECT_UNAUTHORIZED"];

  const bodyString =
    greeting +
    " " +
    "We have entered " +
    res.rowCount +
    "which should match data: " +
    rowCount;

  return { body: bodyString };
}
```

A couple of notes. Now that we expect input to insert data into the database, this function needs to be called where you can pass data. You can do a curl command:

```sh
> curl --request POST \
  --url https://your-server.ondigitalocean.app/forms/form \
  --data '{
  "formId": "b863745d-53a7-4282-a286-fbd8388ba001",
  "data": [
    {
      "question": "question 1",
      "answer": "This is answer 1"
    },
    {
      "question": "question 2",
      "answer": "This is answer 2"
    }
  ]
}'
```

You can also use a tool like Postman or Bruno to send in the request.

Run it, test it, and check your database. Data should now be hitting your database.

## Conclusion

By the end of this point, the entire backend is up and ready to put data into a database. What is missing is the front-end side of the Hugo Project. Part 6 will focus on putting the form together and adding the JavaScript on the form side for submission.
