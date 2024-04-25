#!/bin/bash

# Make a POST request to 0.0.0.0:5000/catch_me with curl
curl -s -X POST "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool"
