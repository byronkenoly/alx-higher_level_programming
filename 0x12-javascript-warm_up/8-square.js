#!/usr/bin/node

let x = parseInt(process.argv[2])

if (isNaN(x) == true || x == null){
    console.log("Missing size");
} else {
    for (let i = 0; i < x; i++){
        let row = '';
        for (let j = 0; j < x; j++){
            row += "X";
        }
        console.log(row);
    }
}
