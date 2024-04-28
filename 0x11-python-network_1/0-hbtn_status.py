#!/usr/bin/python3
# Python script that fetches the URL and read the response.
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    response_body = response.read().decode('utf-')
    for line in response_body.split("\n"):
        print("\t-" + line)
