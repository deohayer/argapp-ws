from .core import *


def test_0_0000():
    # Normal value.
    o = App()
    o.help = 'help'
    assert o.help == 'help'


def test_defaults_1_0000():
    o = App(help='app')
    o.help = None
    assert o.help == ''


def test_exceptions_1_0000():
    o = App()
    with pytest.raises(TypeError) as e:
        o.help = 1.
    assert str(e.value) == str(
        'App.help: Invalid type: float. '
        'Must be: str, None.')
