#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# Use curl to send a request and pipe the response body to wc to count the bytes
SIZE=$(curl -s "$URL" | wc -c)

echo "The size of the response body is: $SIZE bytes"
