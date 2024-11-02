#!/usr/bin/python3
"""Contains validUTF8 function that validate UTF-8 encoding"""


def checkMultiByte(byte):
    """Checks number of bytes in a multi-byte UTF-8 character"""
    mask = 15
    shifted_value = byte >> 4
    bitwiseAND = shifted_value & mask

    if bitwiseAND == 12:
        return 2
    if bitwiseAND == 14:
        return 3
    if bitwiseAND == 15:
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
    for i in range(len(data)):
        data_8LSB = data[i] & 255
        if data_8LSB > 127:
            bytes = checkMultiByte(data_8LSB)
            if bytes == 0:
                return False
            if not evaluateMultiByte(data, i + 1, bytes - 1):
                return False
            i += bytes
    return True
