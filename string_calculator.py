import re

def _parse_delimiter(numbers: str):
    """Extract delimiter and number string."""
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        if len(parts) < 2 or not parts[0][2:]:
            raise ValueError("Custom delimiter definition must be followed by a delimiter and newline.")
        custom_delim = parts[0][2:]
        if custom_delim.isdigit():
            raise ValueError("Custom delimiter cannot be a digit.")
        delimiter = re.escape(custom_delim)
        num_str = parts[1]
    else:
        delimiter = ",|\n"
        num_str = numbers
    return delimiter, num_str

def _extract_tokens(num_str: str, delimiter: str):
    """Split numbers string into tokens, stripping whitespace."""
    return [token.strip() for token in re.split(delimiter, num_str) if token.strip()]

def _check_negatives(tokens):
    """Raise ValueError if any negative numbers are found."""
    negatives = [token for token in tokens if re.fullmatch(r'-\d+', token)]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(negatives)}")

def _sum_tokens(tokens):
    """Sum integer tokens, raise ValueError for invalid input."""
    try:
        return sum(int(token) for token in tokens)
    except ValueError:
        raise ValueError("Invalid input: all values must be integers.")

def add(numbers: str) -> int:
    """
    Adds numbers provided in a comma-separated string or with custom delimiters.
    """
    if not numbers or numbers.strip() == "":
        return 0
    delimiter, num_str = _parse_delimiter(numbers)
    tokens = _extract_tokens(num_str, delimiter)
    _check_negatives(tokens)
    return _sum_tokens(tokens)