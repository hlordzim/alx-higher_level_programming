#!/usr/bin/node
// Import the 'request' module
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    const count = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);
    console.log(count);
  }
});
