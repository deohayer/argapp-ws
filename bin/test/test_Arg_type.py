from .core import *


def test_0_0000():
    o = Arg()
    o.type = int
    assert o.type is int


def test_defaults_1_0000():
    o = Arg(count=0, sopt='o')
    o.type = int
    assert o.type is bool


def test_defaults_2_0000():
    o = Arg()
    o.default = [5]
    assert o.type is int


def test_defaults_3_0000():
    o = Arg()
    o.default = False
    assert o.type is bool


def test_defaults_4_0000():
    o = Arg(type=int)
    o.type = None
    assert o.type is str


def test_defaults_4_0001():
    o = Arg(type=int, default=[])
    o.type = None
    assert o.type is str


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.type = 1.
    assert str(e.value) == str(
        'Arg.type: Invalid type: float. '
        'Must be: type, None.'
    )


def test_exceptions_2_0000():
    o = Arg(default=6)
    with pytest.raises(ValueError) as e:
        o.type = float
    assert str(e.value) == str(
        'Arg.type: Invalid value: float. '
        'Must match self.default: int.'
    )
