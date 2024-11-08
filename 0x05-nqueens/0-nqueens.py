#!/usr/bin/python3
"""N queens puzzle"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

queens = 0
positions = []

while queens < N:
    if len(positions) > 0:
        i = positions[-1][0]
