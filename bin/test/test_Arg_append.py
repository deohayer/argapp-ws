from .core import *


def test_0_0000():
    # Normal value.
    o = Arg(sopt='o')
    o.append = True
    assert o.append is True


def test_defaults_1_0000():
    o = Arg(sopt='o', append=True)
    o.sopt = None
    assert o.append is False


def test_defaults_2_0000():
    o = Arg(sopt='o', append=True)
    o.append = None
    assert o.append is False


def test_exceptions_1_0000():
    o = Arg(sopt='o')
    with pytest.raises(TypeError) as e:
        o.append = 1.
    assert str(e.value) == str(
        'Arg.append: Invalid type: float. '
        'Must be: bool, None.'
    )
