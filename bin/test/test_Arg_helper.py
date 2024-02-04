from .core import *


def test_0_0000():
    helper = ArgHelper()
    o = Arg()
    o.helper = helper
    assert o.helper is helper


def test_defaults_1_0000():
    o = Arg(helper=ArgHelper(False, False))
    o.helper = None
    assert o.helper.choices is True
    assert o.helper.default is True


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.helper = 1.
    assert str(e.value) == str(
        'Arg.helper: Invalid type: float. '
        'Must be: ArgHelper, None.'
    )
