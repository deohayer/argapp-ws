from .core import *


def test_0_0000():
    o = Arg()
    o.help = 'help'
    assert o.help == 'help'


def test_defaults_1_0000():
    o = Arg(help='help')
    o.help = None
    assert o.help == ''


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.help = 1.
    assert str(e.value) == str(
        'Arg.help: Invalid type: float. '
        'Must be: str, None.'
    )
