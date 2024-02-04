from .core import *
from argapp import raise_v


def test_exceptions_0_0000():
    # Success.
    raise_v(None, False, '', '')


def test_exceptions_0_0001():
    # Failure.
    with pytest.raises(ValueError) as e:
        raise_v(0, True, 'test_1', 'Must be 1.')
    assert str(e.value) == str(
        'test_1: Invalid value: 0. '
        'Must be 1.'
    )
