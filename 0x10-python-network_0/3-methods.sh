#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept
# -I flag fetches the headers only

methods=$(curl -sI $1 | grep -i Allow | cut -d' ' -f2-)

echo $methods