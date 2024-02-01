from .core import *


def test_0():
    o = Arg(restrict=False)
    assert o.restrict is False


def test_1():
    o = Arg()
    o.restrict = False
    assert o.restrict is False


def test_defaults_1_0():
    o = Arg()
    assert o.restrict is True


def test_defaults_1_1():
    o = Arg(restrict=False)
    o.restrict = None
    assert o.restrict is True


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(restrict=1.)
    assert str(e.value) == str(
        'Arg.restrict: Invalid type: float. Must be: bool, None.')


def test_exceptions_1_1():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.restrict = 1
    assert str(e.value) == str(
        'Arg.restrict: Invalid type: int. Must be: bool, None.')
