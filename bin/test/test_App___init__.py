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
