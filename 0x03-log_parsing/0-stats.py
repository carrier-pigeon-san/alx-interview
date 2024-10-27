#!/usr/bin/python3
"""A script that reads stin line by line and computes the metrics"""
import sys
import re

try:
    line_count = 1
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    "404": 0, "405": 0, "500": 0}
    log_entry = (
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] '
        r'"GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
    )
    total_size = 0
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        match = re.match(log_entry, line)
        if match:
            total_size += int(match.group("size"))
            status = match.group("status")
            if status in status_codes:
                status_codes[status] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in status_codes.items():
                if val > 0:
                    print("{}: {}".format(int(key), val))

        line_count += 1

except KeyboardInterrupt as err:
    print("File size: {}".format(total_size))
    for key, val in status_codes.items():
        if val > 0:
            print("{}: {}".format(int(key), val))
    raise err
