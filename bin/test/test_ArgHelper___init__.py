from .core import *


def test_description_1_0000():
    # Default.
    o = ArgHelper()
    assert o.choices is True
    assert o.default is True


def test_description_1_0001():
    # All.
    o = ArgHelper(
        default=False,
        choices=False,
    )
    assert o.choices is False
    assert o.default is False


def test_parameters_1_0000():
    # test_0_0000
    assert ArgHelper(choices=False).choices is False


def test_parameters_1_0001():
    # test_defaults_0_0000
    assert ArgHelper(choices=None).choices is True


def test_parameters_1_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        ArgHelper(choices=1.)
    assert str(e.value) == str(
        'ArgHelper.choices: Invalid type: float. '
        'Must be: bool, None.')


def test_parameters_2_0000():
    # test_0_0000
    assert ArgHelper(default=False).default is False


def test_parameters_2_0001():
    # test_defaults_0_0000
    assert ArgHelper(default=None).default is True


def test_parameters_2_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        ArgHelper(default=1.)
    assert str(e.value) == str(
        'ArgHelper.default: Invalid type: float. '
        'Must be: bool, None.')
