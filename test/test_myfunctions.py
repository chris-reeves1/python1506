# pytest
# plain assert statement
# flexibility, integration (runs against unittest test cases)
# automatic test detection
# fixtures - set certain conditionals, paraatisation - pass through multiple sets of data.

import pytest
from pytest_files.my_functions import *

def test_answer():
    result = add(1, 2)
    assert result == 3
    assert add(1, 2) == 3
    assert add(1, 2) == 1 + 2
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(1000, 2000) == 3000


def test_divide():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# class based tests

class Test_area:

    def setup_method(self):
        self.x = Area(5,10)
    
    def test_area(self):
        self.x.area_calc() == 50

    def teardown_method(self):
        del self.x

# # fixture
# def x():
#     return Area((10,5))

# def test_x(x):
#     assert x.area_calc() == 50

# paramatisation

@pytest.mark.parametrize("width, length, area", [(5, 10, 50), (10, 10, 100), (5, 5, 25)])
def test_multiple_areas(width, length, area):
    x = Area(width, length)
    assert x.area_calc() == area

@pytest.mark.skip(reason="something")
def test_b():
    assert add(1, 2) == 3

@pytest.mark.xfail(reason="broken")
def test_a():
    assert add(1, 2) == 3







