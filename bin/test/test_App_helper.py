from .core import *


def test_0_0000():
    # Normal value.
    a = AppHelper()
    o = App()
    o.helper = a
    assert o.helper is a


def test_defaults_1_0000():
    a = AppHelper()
    o = App(helper=a)
    o.helper = None
    assert o.helper.lopt == 'help'
    assert o.helper.sopt == 'h'
    assert o.helper.help == 'Show the help text and exit.'
    assert o.helper is not a


def test_exceptions_1_0000():
    o = App()
    with pytest.raises(TypeError) as e:
        o.helper = 1.
    assert str(e.value) == str(
        'App.helper: Invalid type: float. '
        'Must be: AppHelper, None.')
