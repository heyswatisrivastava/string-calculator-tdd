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

    def test_negative_numbers(self):
        """
        Test that negative numbers raise an exception listing all negatives.
        """
        with self.assertRaises(ValueError) as context:
            add("1,-2,-3,4")
        self.assertIn("negative numbers not allowed -2,-3", str(context.exception))

    def test_custom_delimiter_with_invalid_input(self):
        """
        Test that custom delimiter with invalid input raises ValueError.
        """
        with self.assertRaises(ValueError):
            add("//;\n1;X;3")

    def test_multiple_custom_delimiters_not_supported(self):
        """
        Test that multiple custom delimiters are not supported and raise ValueError.
        """
        with self.assertRaises(ValueError):
            add("//;,\n1;2,3")

    def test_negative_numbers_with_custom_delimiter(self):
        """
        Test that negative numbers with custom delimiter raise exception listing all negatives.
        """
        with self.assertRaises(ValueError) as context:
            add("//;\n-1;2;-3")
        self.assertIn("negative numbers not allowed -1,-3", str(context.exception))

    def test_empty_number_between_delimiters(self):
        """
        Test that empty numbers between delimiters are ignored.
        """
        self.assertEqual(add("1,,2"), 3)
    
    def test_whitespace_handling(self):
        """
        Test that numbers with extra whitespace are handled correctly.
        """
        self.assertEqual(add(" 1 , 2 "), 3)
    
    def test_missing_custom_delimiter_definition(self):
        """
        Test that a custom delimiter prefix without a delimiter raises ValueError.
        """
        with self.assertRaises(ValueError):
            add("//\n1;2")
    
    def test_custom_delimiter_missing_numbers(self):
        """
        Test that a custom delimiter definition with no numbers returns 0.
        """
        self.assertEqual(add("//;\n"), 0)

    def test_only_delimiters_no_numbers(self):
        """
        Test that a string with only delimiters returns 0.
        """
        self.assertEqual(add(",,,"), 0)
    
    def test_non_numeric_with_custom_delimiter(self):
        """
        Test that non-numeric input with custom delimiter raises ValueError.
        """
        with self.assertRaises(ValueError):
            add("//|\n1|two|3")
    
    def test_negative_number_with_whitespace(self):
        """
        Test that negative numbers with whitespace are detected.
        """
        with self.assertRaises(ValueError) as context:
            add("1, -2,3")
        self.assertIn("negative numbers not allowed -2", str(context.exception))
        
if __name__ == "__main__":
    # Run all unit tests
    unittest.main()