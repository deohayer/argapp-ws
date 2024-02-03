from .core import *


def test_description_1_0():
    o = Arg(sopt='o', suppress=True)
    assert o.suppress is True


def test_description_1_1():
    o = Arg(sopt='o')
    o.suppress = True
    assert o.suppress is True


def test_defaults_1_0():
    o = Arg()
    assert o.suppress is False


def test_defaults_1_1():
    o = Arg(sopt='o', suppress=True)
    o.sopt = None
    assert o.suppress is False


def test_defaults_2_0():
    o = Arg(sopt='o')
    assert o.suppress is False


def test_defaults_2_1():
    o = Arg(sopt='o', suppress=True)
    o.suppress = None
    assert o.suppress is False


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(sopt='o', suppress=1.)
    assert str(e.value) == str(
        'Arg.suppress: Invalid type: float. '
        'Must be: bool, None.')


def test_exceptions_1_1():
    o = Arg(sopt='o')
    with pytest.raises(TypeError) as e:
        o.suppress = 1
    assert str(e.value) == str(
        'Arg.suppress: Invalid type: int. '
        'Must be: bool, None.')
