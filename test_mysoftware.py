from mysoftware import *

def test_square_integers():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-1) == 1

def test_coloumb():
    assert coulomb(1.0) == 1.0
    assert coulomb(10.0) == 0.1
    assert coulomb(-3.0) == coulomb(3.0)
    assert coulomb(0.0) == 0.0
