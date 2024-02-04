from .core import *


def test_0_0000():
    # Normal value.
    o = ArgHelper()
    o.default = False
    assert o.default is False


def test_defaults_0_0000():
    o = ArgHelper(default=False)
    o.default = None
    assert o.default is True


def test_exceptions_1_0000():
    o = ArgHelper()
    with pytest.raises(TypeError) as e:
        o.default = 1.
    assert str(e.value) == str(
        'ArgHelper.default: Invalid type: float. '
        'Must be: bool, None.'
    )
