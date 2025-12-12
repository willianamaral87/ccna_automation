from port_validator import PortValidator

def test_valid_port_22():
    v = PortValidator()
    assert v.is_valid_port(202) is True

def test_valid_port_80():
    v = PortValidator()
    assert v.is_valid_port(80) is True

def test_invalid_port_zero():
    v = PortValidator()
    assert v.is_valid_port(0) is False

def test_invalid_port_too_high():
    v = PortValidator()
    assert v.is_valid_port(70000) is False

def test_invalid_port_string():
    v = PortValidator()
    assert v.is_valid_port("80") is False
