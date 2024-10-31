# UTF-8 Validation

This project involves creating a method to validate whether a given data set represents a valid UTF-8 encoding.

## Project Structure

- `0-validate_utf8.py`: Python script containing the function to validate UTF-8 encoding.
- `README.md`: This file, providing an overview of the project.

## Function Details

### validate_utf8(data)

This function takes a list of integers and returns `True` if the data set represents a valid UTF-8 encoding, otherwise returns `False`.

#### Parameters:
- `data` (list): A list of integers representing the data set.

#### Returns:
- `bool`: `True` if the data set is valid UTF-8, `False` otherwise.

## Usage

To use the `validate_utf8` function, import it into your script and pass the data set as an argument:

```python
from 0-validate_utf8 import validate_utf8

data = [197, 130, 1]
print(validate_utf8(data))  # Output: True
```

## Example

```python
data1 = [197, 130, 1]
data2 = [235, 140, 4]

print(validate_utf8(data1))  # Output: True
print(validate_utf8(data2))  # Output: False
```

## Author

Sandy O.