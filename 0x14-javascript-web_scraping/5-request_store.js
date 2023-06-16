#!/usr/bin/node
// Script that gets contents of webpage and stores it in a file

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
