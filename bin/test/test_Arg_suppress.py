from .core import *


def test_0_0000():
    o = Arg(sopt='o')
    o.suppress = True
    assert o.suppress is True


def test_defaults_1_0000():
    o = Arg(suppress=True, sopt='o')
    o.sopt = None
    assert o.suppress is False


def test_defaults_2_0000():
    o = Arg(suppress=True, sopt='o')
    o.suppress = None
    assert o.suppress is False


def test_exceptions_1_0000():
    o = Arg(sopt='o')
    with pytest.raises(TypeError) as e:
        o.suppress = 1.
    assert str(e.value) == str(
        'Arg.suppress: Invalid type: float. '
        'Must be: bool, None.')
