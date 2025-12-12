import unittest
from vlan_validator import VlanValidator

class TestVlanValidator(unittest.TestCase):

    def setUp(self):
        self.validator = VlanValidator()

    def test_valid_vlan(self):
        self.assertTrue(self.validator.is_valid_vlan(10))

    def test_invalid_vlan_zero(self):
        self.assertFalse(self.validator.is_valid_vlan(0))

    def test_invalid_vlan_too_high(self):
        self.assertFalse(self.validator.is_valid_vlan(5000))

    def test_invalid_vlan_string(self):
        self.assertFalse(self.validator.is_valid_vlan("10"))

if __name__ == "__main__":
    unittest.main()
