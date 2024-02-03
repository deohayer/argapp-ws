from .core import *


def test_description_0_0():
    a = AppHelper()
    o = App()
    o.helper = a
    assert o.helper is a


def test_defaults_1_0():
    a = AppHelper()
    o = App(helper=a)
    o.helper = None
    assert isinstance(o.helper, AppHelper)
    assert o.helper is not a


def test_exceptions_1_0():
    o = App()
    with pytest.raises(TypeError) as e:
        o.helper = 1.
    assert str(e.value) == str(
        'App.helper: Invalid type: float. '
        'Must be: AppHelper, None.')
