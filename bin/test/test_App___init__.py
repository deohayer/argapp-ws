from .core import *


def test_description_0():
    # Default.
    o = App()
    assert o.name == ''
    assert o.help == ''
    assert o.prolog == ''
    assert o.epilog == ''
    assert isinstance(o.helper, AppHelper)
    assert o.args == []
    assert o.apps == []


def test_description_1():
    # All.
    a = AppHelper()
    o = App(
        name='name',
        help='help',
        prolog='prolog',
        epilog='epilog',
        helper=a)
    assert o.name == 'name'
    assert o.help == 'help'
    assert o.prolog == 'prolog'
    assert o.epilog == 'epilog'
    assert o.helper is a
    assert o.args == []
    assert o.apps == []


def test_parameters_0_0():
    o = App(name='app')
    assert o.name == 'app'


def test_parameters_0_1():
    o = App()
    assert o.name == ''


def test_parameters_0_2():
    with pytest.raises(TypeError) as e:
        App(name=1.)
    assert str(e.value) == str(
        'App.name: Invalid type: float. '
        'Must be: str, None.')
