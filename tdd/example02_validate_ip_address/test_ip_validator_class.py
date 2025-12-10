# unittest is Python’s built-in testing library.
# It is used to automatically verify that your code works correctly.
import unittest

# Imports the class IPValidator from ip_validator.py file
from ip_validator import IPValidator

class TestIPValidator(unittest.TestCase):
    def setUp(self):
        self.validator = IPValidator()

    def test_valid_ipv4(self):
        self.assertTrue(self.validator.is_valid_ipv4("192.168.1.100"))

    def test_invalid_ipv4_letters(self):
        self.assertFalse(self.validator.is_valid_ipv4("192.abc.1.l"))

    def test_invalid_ipv4_out_of_range(self):
        self.assertFalse(self.validator.is_valid_ipv4("256.100.50.25"))

    def test_invalid_ipv4_too_few_octets(self):
        self.assertFalse(self.validator.is_valid_ipv4("10.10.10"))

    def test_invalid_ipv4_too_many_octets(self):
        self.assertFalse(self.validator.is_valid_ipv4("10.10.10.10.10"))

if __name__ == "__main__":
    unittest.main(verbosity=2)

