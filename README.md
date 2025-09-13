# String Calculator TDD

A simple string calculator implemented using Test-Driven Development (TDD) in Python.

## Features

- Adds numbers provided in a string, separated by commas or newlines.
- Supports custom delimiters (e.g. `//;\n1;2`).
- Handles any amount of numbers.
- Throws an exception for negative numbers, listing all negatives.
- Ignores empty tokens and whitespace.
- Raises `ValueError` for invalid input (non-numeric values or malformed delimiter definitions).

## Usage

### Calculator Function

Import and use the `add` function:

```python
from string_calculator import add

result = add("1,2,3")  # Returns 6
result = add("//;\n1;2")  # Returns 3
```

### Running Tests

All tests are in `test_string_calculator.py`.  
To run the tests, use:

```sh
python -m unittest test_string_calculator.py
```

### Test Coverage

To check test coverage, install the requirements first:

```sh
pip install -r requirements.txt
```

Then run:

```sh
coverage run -m unittest test_string_calculator.py
coverage report
```

## Example Inputs & Outputs

| Input              | Output | Notes                                 |
|--------------------|--------|---------------------------------------|
| `""`               | `0`    | Empty string returns 0                |
| `"1"`              | `1`    | Single number                         |
| `"1,5"`            | `6`    | Two numbers                           |
| `"1\n2,3"`         | `6`    | Newline and comma as delimiters       |
| `"//;\n1;2"`       | `3`    | Custom delimiter `;`                  |
| `"1,-2,-3,4"`      | Error  | Lists all negative numbers            |
| `"1,a,3"`          | Error  | Invalid input                         |

## Project Structure

```
string-calculator-tdd/
├── string_calculator.py
├── test_string_calculator.py
├── requirements.txt
└── README.md
```

## License

MIT