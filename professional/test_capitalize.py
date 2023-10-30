import pytest

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)


def invert_string(x):
    if not isinstance(x,str):
        raise TypeError('Please provide a string argument')
    return x[::-1]

def test_invert_string():
    assert invert_string('Happy') == 'yppaH'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        invert_string(314)