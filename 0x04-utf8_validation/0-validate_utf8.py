#!/usr/bin/python3
"""Contains validUTF8 function that validate UTF-8 encoding"""


def validUTF8(data):
    """Validates UTF-8 encoding"""
    bytes = 0
    for num in data:
        byte = num & 0b11111111
        if bytes:
            if byte >> 6 != 0b10:
                return False
            bytes -= 1
            continue
        else:
            if byte >> 5 == 0b110:
                bytes = 1
            elif byte >> 4 == 0b1110:
                bytes = 2
            elif byte >> 3 == 0b11110:
                bytes = 3
            elif byte >> 7:
                return False
    return bytes == 0
