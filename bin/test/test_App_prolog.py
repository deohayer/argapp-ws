from .core import *


def test_0_0000():
    # Normal value.
    o = App()
    o.prolog = 'prolog'
    assert o.prolog == 'prolog'


def test_defaults_1_0000():
    # Default without help.
    o = App(prolog='prolog')
    o.prolog = None
    assert o.prolog == ''


def test_defaults_1_0001():
    # Default with help.
    o = App(
        help='help',
        prolog='prolog',
    )
    o.prolog = None
    assert o.prolog == 'help'


def test_exceptions_1_0000():
    o = App()
    with pytest.raises(TypeError) as e:
        o.prolog = 1.
    assert str(e.value) == str(
        'App.prolog: Invalid type: float. '
        'Must be: str, None.')
