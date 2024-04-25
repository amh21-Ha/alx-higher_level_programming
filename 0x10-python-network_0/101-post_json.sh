#!/bin/bash

# Check if the correct number of arguments was provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# The filename provided as the second argument
FILENAME=$2

# Ensure the file exists
if [ ! -f "$FILENAME" ]; then
    echo "Error: File does not exist."
    exit 1
fi

# Use curl to send a POST request with the contents of the file as the body
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" -d @"$FILENAME" "$URL")

# Display the body of the response
echo "Response body:"
echo "$RESPONSE"

