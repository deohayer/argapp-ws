from .core import *


def test_description_1_0():
    c = CompleterList(['a', 'b', 'c'])
    o = Arg(completer=c)
    assert o.completer is c


def test_description_1_1():
    c = CompleterList(['a', 'b', 'c'])
    o = Arg()
    o.completer = c
    assert o.completer is c


def test_defaults_1_0():
    o = Arg(choices=[1, 2, 3])
    assert isinstance(o.completer, CompleterList)


def test_defaults_1_1():
    o = Arg()
    o.choices = [1, 2, 3]
    assert isinstance(o.completer, CompleterList)


def test_defaults_2_0():
    o = Arg()
    assert isinstance(o.completer, CompleterPath)


def test_defaults_2_1():
    o = Arg(type=int)
    o.type = str
    assert isinstance(o.completer, CompleterPath)


def test_defaults_3_0():
    o = Arg(type=int)
    assert isinstance(o.completer, CompleterNone)


def test_defaults_3_1():
    o = Arg(type=str)
    o.type = int
    assert isinstance(o.completer, CompleterNone)


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(completer=1.)
    assert str(e.value) == str(
        'Arg.completer: Invalid type: float. '
        'Must be: Completer, None.')


def test_exceptions_1_1():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.completer = []
    assert str(e.value) == str(
        'Arg.completer: Invalid type: list. '
        'Must be: Completer, None.')
