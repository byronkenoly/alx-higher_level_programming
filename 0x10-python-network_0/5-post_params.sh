#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# -d option used to set a body key-value parameter

email="test@gmail.com"
subject="I will always be here for PLD"

curl -sS -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=$email&subject=$subject" $1