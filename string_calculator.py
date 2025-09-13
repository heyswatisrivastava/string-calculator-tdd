import re

def add(numbers: str) -> int:
    """
    Adds numbers provided in a comma-separated string.

    Args:
        numbers (str): A string containing comma-separated numbers.

    Returns:
        int: The sum of the numbers. Returns 0 for an empty string.
    Raises:
        ValueError: If any input is not a valid integer.
    """
    if numbers == "":
        return 0
    # Replace newlines with commas for uniform splitting
    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        numbers = parts[1]
    # Split using the delimiter(s)
    tokens = re.split(delimiter, numbers)
    try:
        return sum(int(n) for n in tokens if n.strip())
    except ValueError:
        raise ValueError("Invalid input: all values must be integers.")