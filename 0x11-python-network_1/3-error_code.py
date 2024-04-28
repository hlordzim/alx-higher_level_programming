#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays the body of the response """

import urllib.request
import urllib.error
import sys
url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:

        response_body = response.read().decode('utf-8')

        print(response_body)

except urllib.error.HTTPError as e:
    print(e.code)
