from .core import *


def test_0_0000():
    o = Arg(sopt='o')
    o.required = False
    assert o.required is False


def test_defaults_1_0000():
    o = Arg(required=False, sopt='o')
    o.sopt = None
    assert o.required is True


def test_defaults_2_0000():
    o = Arg(required=True, sopt='o')
    o.required = None
    assert o.required is False


def test_exceptions_1_0000():
    o = Arg(sopt='o')
    with pytest.raises(TypeError) as e:
        o.required = 1.
    assert str(e.value) == str(
        'Arg.required: Invalid type: float. '
        'Must be: bool, None.')
