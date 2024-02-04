from .core import *


def test_description_0_0000():
    o = CallError()
    o.code = 2
    assert o.code == 2


def test_description_0_0001():
    o = CallError()
    o.code = 0
    assert o.code == 0


def test_defaults_1_0000():
    o = CallError(code=2)
    o.code = None
    assert o.code == 1


def test_exceptions_1_0000():
    o = CallError()
    with pytest.raises(TypeError) as e:
        o.code = 1.
    assert str(e.value) == str(
        'CallError.code: Invalid type: float. '
        'Must be: int, None.')


def test_exceptions_2_0000():
    o = CallError()
    with pytest.raises(ValueError) as e:
        o.code = 256
    assert str(e.value) == str(
        'CallError.code: Invalid value: 256. '
        'Must be from 0 to 255.')
