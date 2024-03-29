#!/usr/bin/node
// script that displays status code of get request

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
