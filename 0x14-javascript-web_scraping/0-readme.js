#!/usr/bin/node
// Script that reads & prints content of a file

const fs = require('fs').promises;

async function readFile (file) {
  try {
    const data = await fs.readFile(file, 'utf-8');
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}

readFile(process.argv[2]);
