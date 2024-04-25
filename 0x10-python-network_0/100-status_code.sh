#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
URL=$1
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $URL)
echo "$RESPONSE"
