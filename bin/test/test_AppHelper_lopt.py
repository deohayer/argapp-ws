from .core import *


def test_description_0_0():
    o = AppHelper()
    o.lopt = 'lopt'
    assert o.lopt == 'lopt'


def test_defaults_1_0():
    o = AppHelper()
    o.lopt = None
    assert o.lopt == ''


def test_exceptions_1_0():
    o = AppHelper()
    with pytest.raises(TypeError) as e:
        o.lopt = 1.
    assert str(e.value) == str(
        'AppHelper.lopt: Invalid type: float. '
        'Must be: str, None.')
