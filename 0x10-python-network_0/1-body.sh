#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL,
#  and displays the body of the response
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
URL=$1
RESPONSE=$(curl -s $URL)
if [ -z "$RESPONSE" ]; then
	echo "Error: Response is empty"
	echo "Debug Info:"
	curl -v $URL 2>&1 | grep '<\|>'
else
	echo "$RESPONSE"
fi
