#!/usr/bin/node
// script that prints title of star wars movie

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log(`${res.statusCode} error`);
  }
});
