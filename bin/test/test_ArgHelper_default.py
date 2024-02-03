from .core import *


def test_description_1_0():
    o = ArgHelper(default=False)
    assert o.default is False


def test_description_1_1():
    o = ArgHelper()
    o.default = False
    assert o.default is False


def test_defaults_1_0():
    o = ArgHelper()
    assert o.default is True


def test_defaults_1_1():
    o = ArgHelper(default=False)
    o.default = None
    assert o.default is True


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        ArgHelper(default=1.)
    assert str(e.value) == str(
        'ArgHelper.default: Invalid type: float. '
        'Must be: bool, None.')


def test_exceptions_1_1():
    o = ArgHelper()
    with pytest.raises(TypeError) as e:
        o.default = 1.
    assert str(e.value) == str(
        'ArgHelper.default: Invalid type: float. '
        'Must be: bool, None.')
