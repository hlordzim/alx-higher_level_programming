#!/usr/bin/python3
# A python script that takes in a URL and an email
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    response_body = response.read().decode('utf-8')
    print(response_body)

