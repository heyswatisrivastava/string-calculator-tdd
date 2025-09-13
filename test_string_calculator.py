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

if __name__ == "__main__":
    # Run all unit tests
    unittest.main()