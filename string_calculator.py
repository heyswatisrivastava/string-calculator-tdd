def add(numbers: str) -> int:
    """
    Adds numbers provided in a comma-separated string.

    Args:
        numbers (str): A string containing comma-separated numbers.

    Returns:
        int: The sum of the numbers. Returns 0 for an empty string.
    """
    # Return 0 if the input string is empty
    if numbers == "":
        return 0