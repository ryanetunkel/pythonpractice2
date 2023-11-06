import pytest


@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200


# Specific file:
# pytest <filename> -v

# Tests with string in its name
# pytest -k <substring> -v

# To stop execution of test suite soon after n number of test fails is as follows
# pytest --maxfail = <num>

# Can run tests by using syntax pytest -n <num> assuming have ran "pip install pytest-xdist"

# generating xml file from running pytest
# pytest test_multiplication.py -v --junitxml="result.xml"

# <testsuit> in the xml files summarises there were 4 tests and the number of failures are 1 (could be dif due to inclusion of wallet)
# <testcase> gives the deatils of each executed test
# <failure> gives the details of the failed test code