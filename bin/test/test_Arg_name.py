from .core import *


def test_0():
    o = Arg(name='ARG')
    assert o.name == 'ARG'


def test_1():
    o = Arg()
    o.name = 'ARG'
    assert o.name == 'ARG'


def test_defaults_1():
    # Constructor.
    o = Arg(lopt='lopt', sopt='s')
    assert o.name == 'LOPT'
    o = Arg(lopt='lopt')
    assert o.name == 'LOPT'
    # Assignment.
    o = Arg()
    o.lopt = 'lopt'
    assert o.name == 'LOPT'
    o.sopt = 'o'
    assert o.name == 'LOPT'
    o.lopt = 'arg'
    assert o.name == 'ARG'
    o.sopt = None
    o.lopt = None
    o.lopt = 'ArG'
    assert o.name == 'ARG'


def test_defaults_2():
    # Constructor.
    o = Arg(sopt='s')
    assert o.name == 'S'
    # Assignment.
    o = Arg()
    o.sopt = 's'
    assert o.name == 'S'
    o.sopt = None
    assert o.name == ''
    o.sopt = 'o'
    assert o.name == 'O'


def test_defaults_3():
    # Constructor.
    o = Arg()
    assert o.name == ''
    # Assignment.
    o = Arg(lopt='lopt', sopt='o')
    o.lopt = None
    o.sopt = None
    assert o.name == ''


def test_exceptions_1():
    m = 'Arg.name: Invalid type: float. Must be: str, None.'
    # Constructor.
    with pytest.raises(TypeError) as e:
        o = Arg(name=1.)
    assert str(e.value) == m
    # Assignment.
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.name = 1.
    assert str(e.value) == m
