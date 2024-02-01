from .core import *


def test_defaults_1():
    # Constructor.
    o = Arg(sopt='s')
    assert o.positional is False
    o = Arg(lopt='lopt')
    assert o.positional is False
    # Assignment.
    o = Arg()
    o.sopt = 's'
    assert o.positional is False
    o = Arg()
    o.lopt = 'lopt'
    assert o.positional is False


def test_defaults_2():
    # Constructor.
    o = Arg()
    assert o.positional is True
    # Assignment.
    o = Arg(sopt='o')
    o.sopt = None
    assert o.positional is True
    o = Arg(lopt='lopt')
    o.lopt = None
    assert o.positional is True
