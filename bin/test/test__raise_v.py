from .core import *
from argapp import _raise_v


def test_0():
    # Success.
    _raise_v(None, True, '', '')


def test_1():
    # Failure.
    with pytest.raises(ValueError) as e:
        _raise_v(0, False, 'test_1', 'Must be 1.')
    assert str(e.value) == str(
        'test_1: Invalid value: 0. Must be 1.')
