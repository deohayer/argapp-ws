from .core import *


def test_0():
    o = Arg(sopt='o')
    assert o.sopt == 'o'


def test_1():
    o = Arg()
    o.sopt = 'o'
    assert o.sopt == 'o'


def test_2():
    o = Arg()
    o.sopt = ''
    assert o.sopt == ''


def test_defaults_1():
    # Constructor.
    o = Arg()
    assert o.sopt == ''
    # Assignment.
    o = Arg(sopt='o')
    o.sopt = None
    assert o.sopt == ''


def test_exceptions_1():
    m = 'Arg.sopt: Invalid type: float. Must be: str, None.'
    # Constructor.
    with pytest.raises(TypeError) as e:
        o = Arg(sopt=1.)
    assert str(e.value) == m
    # Assignment.
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.sopt = 1.
    assert str(e.value) == m


def test_exceptions_2():
    m = 'Arg.sopt: Invalid value: "long". Must not exceed one character.'
    # Constructor.
    with pytest.raises(ValueError) as e:
        o = Arg(sopt='long')
    assert str(e.value) == m
    # Assignment.
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.sopt = 'long'
    assert str(e.value) == m
