from .core import *


def test_0():
    helper = ArgHelper()
    o = Arg(helper=helper)
    assert o.helper is helper


def test_1():
    helper = ArgHelper()
    o = Arg()
    o.helper = helper
    assert o.helper is helper


def test_defaults_1():
    helper = ArgHelper()
    # Constructor.
    o = Arg()
    assert o.helper.choices == helper.choices
    assert o.helper.default == helper.default
    # Assignment.
    o = Arg(helper=ArgHelper(False, False))
    o.helper = None
    assert o.helper.choices == helper.choices
    assert o.helper.default == helper.default


def test_exceptions_1():
    m = 'Arg.helper: Invalid type: float. Must be: ArgHelper, None.'
    # Constructor.
    with pytest.raises(TypeError) as e:
        o = Arg(helper=1.)
    assert str(e.value) == m
    # Assignment.
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.helper = 1.
    assert str(e.value) == m
