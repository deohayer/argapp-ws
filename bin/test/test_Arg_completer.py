from .core import *


def test_0_0000():
    # Normal value.
    completer = CompleterList(['a', 'b', 'c'])
    o = Arg()
    o.completer = completer
    assert o.completer is completer


def test_defaults_1_0000():
    o = Arg()
    o.choices = [1, 2, 3]
    assert isinstance(o.completer, CompleterList)


def test_defaults_2_0000():
    o = Arg(type=int)
    o.type = str
    assert isinstance(o.completer, CompleterPath)


def test_defaults_3_0000():
    o = Arg(type=str)
    o.type = int
    assert isinstance(o.completer, CompleterNone)


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.completer = 1.
    assert str(e.value) == str(
        'Arg.completer: Invalid type: float. '
        'Must be: Completer, None.')
