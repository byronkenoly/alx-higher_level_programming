#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response

status_code=$(curl -sw "%{http_code}" $1 -o /dev/null)

if [[ "$status_code" -eq "200" ]]; then
    curl -s $1
fi