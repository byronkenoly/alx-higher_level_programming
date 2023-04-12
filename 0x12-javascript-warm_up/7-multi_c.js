#!/usr/bin/node

let x = parseInt(process.argv[2])

if (isNaN(x) == true || x == null){
    console.log("Missing number of occurences");
} else {
    for (let i = 0; i < x; i++){
        console.log("C is fun");
    }
}
