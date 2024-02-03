from .core import *


def test_description_1_0():
    o = Arg(sopt='o', required=False)
    assert o.required is False


def test_description_1_1():
    o = Arg(sopt='o')
    o.required = False
    assert o.required is False


def test_defaults_1_0():
    o = Arg()
    assert o.required is True


def test_defaults_1_1():
    o = Arg(sopt='o', required=False)
    o.sopt = None
    assert o.required is True


def test_defaults_2_0():
    o = Arg(sopt='o')
    assert o.required is False


def test_defaults_2_1():
    o = Arg(sopt='o', required=True)
    o.required = None
    assert o.required is False


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(sopt='o', required=1.)
    assert str(e.value) == str(
        'Arg.required: Invalid type: float. '
        'Must be: bool, None.')


def test_exceptions_1_1():
    o = Arg(sopt='o')
    with pytest.raises(TypeError) as e:
        o.required = 1
    assert str(e.value) == str(
        'Arg.required: Invalid type: int. '
        'Must be: bool, None.')
