#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and 
#   displays the size of the body of the response
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
SIZE=$(curl -sI $URL | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
echo "$SIZE"
