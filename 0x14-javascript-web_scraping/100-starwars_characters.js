#!/usr/bin/node

const movieNumber = process.argv.slice(2);
const request = require('request');

if (Number.isInteger(parseInt(movieNumber[0]))) {
  request('http://swapi.co/api/films/' + movieNumber[0], function (error, response, body) {
    if (error) console.error('error:', error);
    JSON.parse(body).characters.forEach(link => request(link, (error, response, body) => {
      if (error) console.error('error:', error);
      console.log(JSON.parse(body).name);
    }));
  });
}
