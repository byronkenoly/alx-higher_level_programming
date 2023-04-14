#!/usr/bin/node

const numero = parseInt(process.argv[2]);

if (isNaN(numero) === true) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numero}`);
}
