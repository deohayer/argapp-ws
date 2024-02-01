from .core import *
from argapp import _raise_t


def test_0():
    # Single type, success.
    _raise_t(1, int, '')


def test_1():
    # Multiple types, success.
    _raise_t(1, (str, int), '')


def test_2():
    # Single type, failure.
    with pytest.raises(TypeError) as e:
        _raise_t(1, float, 'test_2')
    assert str(e.value) == str(
        'test_2: Invalid type: int. Must be: float.')


def test_3():
    # Multiple types, failure.
    with pytest.raises(TypeError) as e:
        _raise_t(1, (float, type(None)), 'test_3')
    assert str(e.value) == str(
        'test_3: Invalid type: int. Must be: float, None.')
