from .core import *


def test_0_0000():
    # Normal value.
    o = AppHelper()
    o.help = 'Help.'
    assert o.help == 'Help.'


def test_defaults_1_0000():
    o = AppHelper()
    o.help = None
    assert o.help == ''


def test_exceptions_1_0000():
    o = AppHelper()
    with pytest.raises(TypeError) as e:
        o.help = 1.
    assert str(e.value) == str(
        'AppHelper.help: Invalid type: float. '
        'Must be: str, None.')
