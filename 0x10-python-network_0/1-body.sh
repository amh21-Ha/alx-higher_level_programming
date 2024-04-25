#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# Use curl to send a GET request and display the body if the status code is 200
RESPONSE=$(curl -s -w "%{http_code}" "$URL")

# Extract the status code from the response
STATUS_CODE=$(echo "$RESPONSE" | tail -n 1)

if [ "$STATUS_CODE" == "200" ]; then
    # Display the body of the response
    BODY=$(echo "$RESPONSE" | sed '$d')  # Remove the last line (status code)
    echo "Response body (200 OK):"
    echo "$BODY"
else
    echo "Error: Non-200 status code received ($STATUS_CODE)"
fi
