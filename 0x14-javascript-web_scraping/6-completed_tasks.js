#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./script.js <API_URL>');
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);
      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completed[todo.userId] === undefined) {
            completed[todo.userId] = 1;
          } else {
            completed[todo.userId]++;
          }
        }
      });

      Object.entries(completed).forEach(([userId, count]) => {
        console.log(`User ID ${userId} has completed ${count} tasks`);
      });
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', error);
  }
});
