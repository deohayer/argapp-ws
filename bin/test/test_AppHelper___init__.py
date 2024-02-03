from .core import *


def test_description_0_0():
    o = AppHelper()
    assert o.sopt == 'h'
    assert o.lopt == 'help'
    assert o.help == 'Show the help text and exit.'


def test_description_0_1():
    o = AppHelper(
        sopt='s',
        lopt='lopt',
        help='Help.')
    assert o.sopt == 's'
    assert o.lopt == 'lopt'
    assert o.help == 'Help.'


def test_parameters_1_0():
    o = AppHelper(lopt='lopt')
    assert o.lopt == 'lopt'


def test_parameters_1_1():
    o = AppHelper(lopt=None)
    assert o.lopt == ''


def test_parameters_1_2():
    with pytest.raises(TypeError) as e:
        AppHelper(lopt=1.)
    assert str(e.value) == str(
        'AppHelper.lopt: Invalid type: float. '
        'Must be: str, None.')
