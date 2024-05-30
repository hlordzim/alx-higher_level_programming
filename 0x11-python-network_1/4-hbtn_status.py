#!/usr/bin/python3
"""       """
import requests

url = 'https://alx-intranet.hbtn.io/status'

# Send a GET request to the URL
response = requests.get(url)

# Display the body of the response with tabulation before each line
response_body_lines = response.text.split("\n")
for line in response_body_lines:
    print("\t-" + line)
