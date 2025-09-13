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
    try:
        return sum(int(n) for n in numbers.split(",") if n.strip())
    except ValueError:
        raise ValueError("Invalid input: all values must be integers.")