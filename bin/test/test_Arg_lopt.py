from .core import *


def test_0():
    o = Arg(lopt='init_lopt')
    assert o.lopt == 'init_lopt'


def test_1():
    o = Arg()
    o.lopt = 'set_lopt'
    assert o.lopt == 'set_lopt'


def test_defaults_1():
    # Constructor.
    o = Arg()
    assert o.lopt == ''
    # Assignment.
    o = Arg(lopt='lopt')
    o.lopt = None
    assert o.lopt == ''


def test_exceptions_1():
    m = 'Arg.lopt: Invalid type: float. Must be: str, None.'
    # Constructor.
    with pytest.raises(TypeError) as e:
        o = Arg(lopt=1.)
    assert str(e.value) == m
    # Assignment.
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.lopt = 1.
    assert str(e.value) == m
