from .core import *
from argapp import raise_t


def test_exceptions_0_0000():
    # Single type, success.
    raise_t(1, int, '')


def test_exceptions_0_0001():
    # Multiple types, success.
    raise_t(1, (str, int), '')


def test_exceptions_0_0002():
    # Single type, failure.
    with pytest.raises(TypeError) as e:
        raise_t(1, float, 'test_2')
    assert str(e.value) == str(
        'test_2: Invalid type: int. '
        'Must be: float.'
    )


def test_exceptions_0_0003():
    # Multiple types, failure.
    with pytest.raises(TypeError) as e:
        raise_t(1, (float, type(None)), 'test_3')
    assert str(e.value) == str(
        'test_3: Invalid type: int. '
        'Must be: float, None.'
    )
