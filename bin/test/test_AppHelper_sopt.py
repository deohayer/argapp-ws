from .core import *


def test_description_0_0():
    o = AppHelper()
    o.sopt = 's'
    assert o.sopt == 's'


def test_defaults_1_0():
    o = AppHelper()
    o.sopt = None
    assert o.sopt == ''


def test_exceptions_1_0():
    o = AppHelper()
    with pytest.raises(TypeError) as e:
        o.sopt = 1.
    assert str(e.value) == str(
        'AppHelper.sopt: Invalid type: float. '
        'Must be: str, None.')


def test_exceptions_2_0():
    o = AppHelper()
    with pytest.raises(ValueError) as e:
        o.sopt = 'long'
    assert str(e.value) == str(
        'AppHelper.sopt: Invalid value: "long". '
        'Must not exceed one character.')
