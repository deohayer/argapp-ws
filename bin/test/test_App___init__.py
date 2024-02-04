from .core import *


def test_0_0000():
    # Default.
    o = App()
    assert o.name == ''
    assert o.help == ''
    assert o.prolog == ''
    assert o.epilog == ''
    assert o.helper.lopt == 'help'
    assert o.helper.sopt == 'h'
    assert o.helper.help == 'Show the help text and exit.'
    assert o.args == []
    assert o.apps == []


def test_0_0001():
    # All.
    helper = AppHelper()
    o = App(
        name='name',
        help='help',
        prolog='prolog',
        epilog='epilog',
        helper=helper,
    )
    assert o.name == 'name'
    assert o.help == 'help'
    assert o.prolog == 'prolog'
    assert o.epilog == 'epilog'
    assert o.helper is helper
    assert o.args == []
    assert o.apps == []


def test_parameters_1_0000():
    # test_0_0000.
    assert App(name='app').name == 'app'


def test_parameters_1_0001():
    # test_defaults_1_0000.
    assert App(name=None).name == ''


def test_parameters_1_0002():
    # test_exceptions_1_0000.
    with pytest.raises(TypeError) as e:
        App(name=1.)
    assert str(e.value) == str(
        'App.name: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_2_0000():
    # test_0_0000.
    assert App(help='help').help == 'help'


def test_parameters_2_0001():
    # test_defaults_1_0000.
    assert App(help=None).help == ''


def test_parameters_2_0002():
    # test_exceptions_1_0000.
    with pytest.raises(TypeError) as e:
        App(help=1.)
    assert str(e.value) == str(
        'App.help: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_3_0000():
    # test_0_0000.
    assert App(prolog='prolog').prolog == 'prolog'


def test_parameters_3_0001():
    # test_defaults_1_0000.
    assert App(prolog=None).prolog == ''


def test_parameters_3_0002():
    # test_defaults_1_0001.
    assert App(help='help').prolog == 'help'


def test_parameters_3_0003():
    # test_exceptions_1_0000.
    with pytest.raises(TypeError) as e:
        App(prolog=1.)
    assert str(e.value) == str(
        'App.prolog: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_4_0000():
    # test_0_0000.
    assert App(epilog='epilog').epilog == 'epilog'


def test_parameters_4_0001():
    # test_defaults_1_0000.
    assert App(epilog=None).epilog == ''


def test_parameters_4_0002():
    # test_exceptions_1_0000.
    with pytest.raises(TypeError) as e:
        App(epilog=1.)
    assert str(e.value) == str(
        'App.epilog: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_5_0000():
    # test_0_0000.
    helper = AppHelper()
    assert App(helper=helper).helper is helper


def test_parameters_5_0001():
    # test_defaults_1_0000.
    o = App(helper=None)
    assert o.helper.lopt == 'help'
    assert o.helper.sopt == 'h'
    assert o.helper.help == 'Show the help text and exit.'


def test_parameters_5_0002():
    # test_exceptions_1_0000.
    with pytest.raises(TypeError) as e:
        App(helper=1.)
    assert str(e.value) == str(
        'App.helper: Invalid type: float. '
        'Must be: AppHelper, None.')
