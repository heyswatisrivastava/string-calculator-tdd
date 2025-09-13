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
        custom_delim = parts[0][2:]
        # If the custom delimiter is a digit, raise ValueError (ambiguous)
        if custom_delim.isdigit():
            raise ValueError("Custom delimiter cannot be a digit.")
        delimiter = re.escape(custom_delim)
        numbers = parts[1]
    tokens = re.split(delimiter, numbers)
    # Report all negative numbers in the error message
    negatives = [int(n) for n in tokens if n.strip() and int(n) < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
    try:
        return sum(int(n) for n in tokens if n.strip())
    except ValueError:
        raise ValueError("Invalid input: all values must be integers.")