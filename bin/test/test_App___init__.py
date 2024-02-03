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


def test_parameters_1_0():
    o = App(help='app')
    assert o.help == 'app'


def test_parameters_1_1():
    o = App()
    assert o.help == ''


def test_parameters_1_2():
    with pytest.raises(TypeError) as e:
        App(help=1.)
    assert str(e.value) == str(
        'App.help: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_3_0():
    o = App(prolog='app')
    assert o.prolog == 'app'


def test_parameters_3_1():
    o = App()
    assert o.prolog == ''


def test_parameters_3_2():
    with pytest.raises(TypeError) as e:
        App(prolog=1.)
    assert str(e.value) == str(
        'App.prolog: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_4_0():
    o = App(epilog='app')
    assert o.epilog == 'app'


def test_parameters_4_1():
    o = App()
    assert o.epilog == ''


def test_parameters_4_2():
    with pytest.raises(TypeError) as e:
        App(epilog=1.)
    assert str(e.value) == str(
        'App.epilog: Invalid type: float. '
        'Must be: str, None.')
