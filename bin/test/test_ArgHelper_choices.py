from .core import *


def test_0_0000():
    # Normal value.
    o = ArgHelper()
    o.choices = False
    assert o.choices is False


def test_defaults_0_0000():
    o = ArgHelper(choices=False)
    o.choices = None
    assert o.choices is True


def test_exceptions_1_0000():
    o = ArgHelper()
    with pytest.raises(TypeError) as e:
        o.choices = 1.
    assert str(e.value) == str(
        'ArgHelper.choices: Invalid type: float. '
        'Must be: bool, None.'
    )
