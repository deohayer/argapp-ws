from .core import *


def test_description_0_0():
    o = App()
    o.epilog = 'epilog'
    assert o.epilog == 'epilog'


def test_defaults_1_0():
    o = App(epilog='epilog')
    o.epilog = None
    assert o.epilog == ''


def test_exceptions_1_0():
    o = App()
    with pytest.raises(TypeError) as e:
        o.epilog = 1.
    assert str(e.value) == str(
        'App.epilog: Invalid type: float. '
        'Must be: str, None.')
