#!/usr/bin/node

let numero = parseInt(process.argv[2])

if (numero == NaN){
    console.log("Not a number");
} else {
    console.log(numero);
}