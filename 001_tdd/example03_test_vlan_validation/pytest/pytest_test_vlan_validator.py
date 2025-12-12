from pytest_vlan_validator import VlanValidator

def test_valid_port_10():
    v = VlanValidator()
    assert v.is_valid_vlan(10) is True

def test_valid_port_100():
    v = VlanValidator()
    assert v.is_valid_vlan(100) is True

def test_valid_port_0():
    v = VlanValidator()
    assert v.is_valid_vlan(0) is False

def test_invalid_port_5000():
    v = VlanValidator()
    assert v.is_valid_vlan(5000) is False

def test_invalid_port_string():
    v = VlanValidator()
    assert v.is_valid_vlan("10") is False
