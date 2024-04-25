#!/bin/bash
# Bash script that takes in a URL and displays all
#  HTTP methods the server will accept
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
URL=$1
METHODS=$(curl -s -X OPTIONS -I $URL | grep "Allow:" | awk -F': ' '{print $2}')
echo "Allowed HTTP Methods for $URL: $METHODS"
