# Island Perimeter

This project folder contains a solution to the "Island Perimeter" problem.

## Problem Description

You are given a grid representing a map where:
- `0` represents water
- `1` represents land

The grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (or one connected component of land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). Each cell is a square with a side length of 1. The grid is rectangular, with its width and height not exceeding 100. Determine the perimeter of the island.

## Example

```plaintext
Input:
[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

Output:
16
```

## Solution

The solution involves iterating through each cell in the grid and calculating the perimeter by checking the adjacent cells.

## Files

- `0-island_perimeter.py`: Contains the function `island_perimeter(grid)` that computes the perimeter of the island.
- `README.md`: This file, providing an overview of the project.

## Usage

To use the function, import it and pass a grid as an argument:

```python
from 0-island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

## Author

Sandy O.