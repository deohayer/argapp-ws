from .core import *


def test_description_0():
    o = App()
    o.name = 'app'
    assert o.name == 'app'


def test_defaults_0_0():
    o = App(name='app')
    o.name = None
    assert o.name == ''


def test_exceptions_0_0():
    o = App()
    with pytest.raises(TypeError) as e:
        o.name = 1.
    assert str(e.value) == str(
        'App.name: Invalid type: float. '
        'Must be: str, None.')
