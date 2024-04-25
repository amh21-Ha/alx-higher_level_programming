#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# The URL provided as the first argument
URL=$1

# Use curl to send an OPTIONS request and extract the Allow header
ALLOW_HEADER=$(curl -s -I -X OPTIONS "$URL" | grep -i "^Allow:")

if [ -n "$ALLOW_HEADER" ]; then
    # Extract the allowed methods from the header
    ALLOWED_METHODS=$(echo "$ALLOW_HEADER" | awk '{print $2}')
    echo "Allowed HTTP methods for $URL:"
    echo "$ALLOWED_METHODS"
else
    echo "Error: Unable to retrieve allowed methods for $URL"
fi
