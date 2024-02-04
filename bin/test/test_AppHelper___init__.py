from .core import *


def test_0_0000():
    # Default.
    o = AppHelper()
    assert o.lopt == 'help'
    assert o.sopt == 'h'
    assert o.help == 'Show the help text and exit.'


def test_0_0001():
    # All.
    o = AppHelper(
        lopt='lopt',
        sopt='s',
        help='Help.',
    )
    assert o.lopt == 'lopt'
    assert o.sopt == 's'
    assert o.help == 'Help.'


def test_parameters_1_0000():
    # test_0_0000
    assert AppHelper(lopt='lopt').lopt == 'lopt'


def test_parameters_1_0001():
    # test_defaults_1_0000
    assert AppHelper(lopt=None).lopt == ''


def test_parameters_1_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        AppHelper(lopt=1.)
    assert str(e.value) == str(
        'AppHelper.lopt: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_2_0000():
    # test_0_0000
    assert AppHelper(sopt='s').sopt == 's'


def test_parameters_2_0001():
    # test_defaults_1_0000
    assert AppHelper(sopt=None).sopt == ''


def test_parameters_2_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        AppHelper(sopt=1.)
    assert str(e.value) == str(
        'AppHelper.sopt: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_2_0003():
    # test_exceptions_2_0000
    with pytest.raises(ValueError) as e:
        AppHelper(sopt='long')
    assert str(e.value) == str(
        'AppHelper.sopt: Invalid value: "long". '
        'Must not exceed one character.')


def test_parameters_1_0000():
    # test_0_0000
    assert AppHelper(help='help').help == 'help'


def test_parameters_1_0001():
    # test_defaults_1_0000
    assert AppHelper(help=None).help == ''


def test_parameters_1_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        AppHelper(help=1.)
    assert str(e.value) == str(
        'AppHelper.help: Invalid type: float. '
        'Must be: str, None.')
