
from series import fibonacci
from series import lucas
from series import sum_series
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
def test_sum_series():
    actual = sum_series(1)
    expected = 1
    assert actual == expected
def test_sum_series2():
    actual = sum_series(2)
    expected=1
    assert actual == expected
def test_sum_series3():
    actual = sum_series(2,2,1)
    expected=3
    assert actual == expected
def test_sum_series4():
    actual = sum_series(3,2,1)
    expected=4
    assert actual == expected