#!/usr/bin/python3
"""Contains validUTF8 function that validate UTF-8 encoding"""


def checkMultiByte(byte):
    """Checks number of bytes in a multi-byte UTF-8 character"""
    mask = 15
    shift = byte >> 4

    if shift & 12 == 12:
        return 2
    if shift & 14 == 14:
        return 3
    if shift & 15 == 15:
        return 4
    return 0


def evaluateMultiByte(data, start, bytes):
    """Evaluates multi-byte UTF-8 characters"""
    range = start + bytes
    multiByte = data[start:range]
    mask = 128
    for byte in multiByte:
        if byte & mask != 128:
            return False
    return True


def validUTF8(data):
    """Validates UTF-8 encoding"""
    i = 0
    while i < len(data):
        byte = data[i] & 0xFF  # Mask to get the 8 least significant bits
        if byte > 127:
            bytes_needed = checkMultiByte(byte)
            if bytes_needed == 0:
                return False
            if not evaluateMultiByte(data, i + 1, bytes_needed - 1):
                return False
            i += bytes_needed
        else:
            i += 1
    return True
