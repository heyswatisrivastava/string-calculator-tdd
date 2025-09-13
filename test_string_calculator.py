import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    """
    Unit tests for the add function in string_calculator.py.
    """

    def test_empty_string(self):
        """
        Test that an empty string returns 0.
        """
        self.assertEqual(add(""), 0)
    
    def test_invalid_input(self):
        """
        Test that invalid input raises a ValueError.
        """
        with self.assertRaises(ValueError):
            add("1,a,3")
    
    def test_newline_delimiter(self):
        """
        Test that new lines between numbers are handled as delimiters.
        """
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        """
        Test that custom delimiters are supported.
        """
        self.assertEqual(add("//;\n1;2"), 3)

if __name__ == "__main__":
    # Run all unit tests
    unittest.main()