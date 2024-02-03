from .core import *


def test_description_1_0():
    o = ArgHelper(choices=False)
    assert o.choices is False


def test_description_1_1():
    o = ArgHelper()
    o.choices = False
    assert o.choices is False


def test_defaults_1_0():
    o = ArgHelper()
    assert o.choices is True


def test_defaults_1_1():
    o = ArgHelper(choices=False)
    o.choices = None
    assert o.choices is True


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        ArgHelper(choices=1.)
    assert str(e.value) == str(
        'ArgHelper.choices: Invalid type: float. '
        'Must be: bool, None.')


def test_exceptions_1_1():
    o = ArgHelper()
    with pytest.raises(TypeError) as e:
        o.choices = 1.
    assert str(e.value) == str(
        'ArgHelper.choices: Invalid type: float. '
        'Must be: bool, None.')
