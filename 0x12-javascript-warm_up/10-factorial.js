#!/usr/bin/node

function factorial (arg) {
  if (isNaN(arg) === true) {
    return 1;
  }

  if (arg == 1) {
    return 1;
  }

  return arg * factorial(arg - 1);
}

const arg = process.argv[2];

console.log(factorial(arg));
