from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_incorrect_add():
    calc = Calculator()
    assert not calc.add(2, 3) == 6

def test_incorrect_subtract():
    calc = Calculator()
    assert not calc.subtract(10, 4) == 70