# Making Change

This project folder contains solutions to the "Making Change" problem, which is a common algorithmic challenge. The goal is to determine the minimum number of coins needed to make a given amount of change.

## Files

- `0-making_change.py`: Python script that contains the function to solve the making change problem.
- `README.md`: This file, providing an overview of the project.

## Function

### `make_change(coins, total)`

This function calculates the minimum number of coins needed to make the given amount of change.

#### Parameters:
- `coins` (list): A list of the values of the coins available.
- `total` (int): The total amount of change needed.

#### Returns:
- `int`: The minimum number of coins needed to make the change, or `-1` if it is not possible to make the change with the given coins.

## Usage

To use the `make_change` function, import it into your script and call it with the appropriate parameters:

```python
from 0-making_change import make_change

coins = [1, 2, 5]
total = 11
print(make_change(coins, total))  # Output: 3
```

## Author

Sandy O.
