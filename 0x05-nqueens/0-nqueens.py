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


def nqueens(N):
    """N queens puzzle"""
    queens = []
    q_cols = []

    def isSafe(x, y):
        """Check if a queen can be placed on x, y"""
        for i in range(len(q_cols)):
            if y == q_cols[i]:
                return False
            if x + y == i + q_cols[i] or x - y == i - q_cols[i]:
                return False
        return True

    def backtrack(x):
        """Backtrack"""
        if x == N:
            queens.append([[r, c] for r, c in enumerate(q_cols)])
            return

        for y in range(N):
            if isSafe(x, y):
                q_cols.append(y)
                backtrack(x + 1)
                q_cols.pop()

    backtrack(0)
    return queens


for board in nqueens(N):
    print(board)
