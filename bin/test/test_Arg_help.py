from .core import *


def test_0():
    o = Arg(help='init_help')
    assert o.help == 'init_help'


def test_1():
    o = Arg()
    o.help = 'set_help'
    assert o.help == 'set_help'


def test_defaults_1():
    # Constructor.
    o = Arg()
    assert o.help == ''
    # Assignment.
    o = Arg(help='help')
    o.help = None
    assert o.help == ''


def test_exceptions_1():
    m = 'Arg.help: Invalid type: float. Must be: str, None.'
    # Constructor.
    with pytest.raises(TypeError) as e:
        o = Arg(help=1.)
    assert str(e.value) == m
    # Assignment.
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.help = 1.
    assert str(e.value) == m
