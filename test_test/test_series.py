
from series import fibonacci
from series import lucas
def test_fibonacci():
    actual = fibonacci(1)
    expected=1
    assert actual == expected
def test_fibonacci2():
    actual = fibonacci(2)
    expected=1
    assert actual == expected

def test_lucas():
    actual = lucas(9)
    expected = 76
    assert actual == expected
def test_lucas2():
    actual = lucas(3)
    expected = 4
    assert actual == expected