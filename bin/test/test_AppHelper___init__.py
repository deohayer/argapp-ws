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


def test_parameters_2_0():
    o = AppHelper(sopt='s')
    assert o.sopt == 's'


def test_parameters_2_1():
    o = AppHelper(sopt=None)
    assert o.sopt == ''


def test_parameters_2_2():
    with pytest.raises(TypeError) as e:
        AppHelper(sopt=1.)
    assert str(e.value) == str(
        'AppHelper.sopt: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_2_3():
    with pytest.raises(ValueError) as e:
        AppHelper(sopt='long')
    assert str(e.value) == str(
        'AppHelper.sopt: Invalid value: "long". '
        'Must not exceed one character.')


def test_parameters_3_0():
    o = AppHelper(help='Help.')
    assert o.help == 'Help.'


def test_parameters_3_1():
    o = AppHelper(help=None)
    assert o.help == ''


def test_parameters_3_2():
    with pytest.raises(TypeError) as e:
        AppHelper(help=1.)
    assert str(e.value) == str(
        'AppHelper.help: Invalid type: float. '
        'Must be: str, None.')
