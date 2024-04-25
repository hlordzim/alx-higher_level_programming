#!/bin/bash
# Bash script that sends a JSON POST request to
# a URL passed as the first argument
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi
URL=$1
JSON_FILE=$2
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: File '$JSON_FILE' not found!"
    exit 1
fi
curl -s -X POST -H "Content-Type: application/json" -d "@$JSON_FILE" $URL
