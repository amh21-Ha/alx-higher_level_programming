#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# Use curl to send a POST request with the required data
RESPONSE=$(curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$URL")

# Display the body of the response
echo "Response body:"
echo "$RESPONSE"
