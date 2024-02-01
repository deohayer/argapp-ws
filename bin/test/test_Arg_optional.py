from .core import *


def test_defaults_1():
    # Constructor.
    o = Arg(sopt='s')
    assert o.optional is True
    o = Arg(lopt='lopt')
    assert o.optional is True
    # Assignment.
    o = Arg()
    o.sopt = 's'
    assert o.optional is True
    o = Arg()
    o.lopt = 'lopt'
    assert o.optional is True


def test_defaults_2():
    # Constructor.
    o = Arg()
    assert o.optional is False
    # Assignment.
    o = Arg(sopt='o')
    o.sopt = None
    assert o.optional is False
    o = Arg(lopt='lopt')
    o.lopt = None
    assert o.optional is False
