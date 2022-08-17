#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const wi = JSON.parse(body).results;
    let y = 0;
    for (const X of wi) {
      for (const char of X.characters) {
        if (char.search('/18/') > 0) {
          y++;
        }
      }
    }
    console.log(y);
  }
});
