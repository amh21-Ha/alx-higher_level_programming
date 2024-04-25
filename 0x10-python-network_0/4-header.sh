#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# Use curl to send a GET request with the custom header
RESPONSE=$(curl -s -H "X-School-User-Id: 98" "$URL")

# Display the body of the response
echo "Response body:"
echo "$RESPONSE"
