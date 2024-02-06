#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics
based on the input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys

""" Initialize variables"""
total_size = 0
status_codes = {}
line_count = 0

try:
    """ Loop through each line of stdin"""
    for line in sys.stdin:
        """ Split the line by spaces"""
        fields = line.split()
        """ Get the status code and file size from the fields"""
        status_code = fields[-2]
        file_size = fields[-1]
        """ Convert the file size to an integer"""
        file_size = int(file_size)
        """ Add the file size to the total size"""
        total_size += file_size
        """ Increment the line count"""
        line_count += 1
        """ Update the status codes dictionary"""
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
        """ Print the metrics every 10 lines """
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes.items()):
                print("{}: {}".format(code, count))
except KeyboardInterrupt:
    """ Handle keyboard interruption"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))
    raise
