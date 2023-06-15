#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs').promises;

async function writeFile(file, data){
    try {
        await fs.writeFile(file, data, 'utf-8');
    } catch (error) {
        console.error(error);
    }
}

writeFile(process.argv[2], process.argv[3]);
