import unittest
from port_number_validator import PortNumberValidator

class TestPortNumberValidator(unittest.TestCase):

    def setUp(self):
        self.validator = PortNumberValidator()

    def test_valid_port(self):
        self.assertTrue(self.validator.is_valid_port(10))

    def test_invalid_port_zero(self):
        self.assertFalse(self.validator.is_valid_port(0))

    def test_invalid_port_too_high(self):
        self.assertFalse(self.validator.is_valid_port(65536))

    def test_invalid_port_string(self):
        self.assertFalse(self.validator.is_valid_port("10"))

if __name__ == "__main__":
    unittest.main()
