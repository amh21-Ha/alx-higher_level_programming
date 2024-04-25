#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# Use curl to send a request and store the response status code
STATUS_CODE=$(curl -o /dev/null -s -w "%{http_code}" "$URL")

# Display the status code
echo "Status code: $STATUS_CODE"

