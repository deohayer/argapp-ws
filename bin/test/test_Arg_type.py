from .core import *


def test_description_1_0():
    o = Arg(type=int)
    assert o.type is int


def test_description_1_1():
    o = Arg()
    o.type = int
    assert o.type is int


def test_defaults_1_0():
    o = Arg(count=0, sopt='o')
    assert o.type is bool


def test_defaults_1_1():
    o = Arg()
    o.sopt = 'o'
    assert o.type is not bool
    o.count = 0
    assert o.type is bool


def test_defaults_1_2():
    o = Arg(count=0, sopt='o')
    o.type = int
    assert o.type is bool


def test_defaults_2_1():
    o = Arg(default=[5])
    assert o.type is int


def test_defaults_2_2():
    o = Arg()
    o.default = [5]
    assert o.type is int


def test_defaults_3_1():
    o = Arg(default=False)
    assert o.type is bool


def test_defaults_3_2():
    o = Arg()
    o.default = False
    assert o.type is bool


def test_defaults_4_0():
    o = Arg()
    assert o.type is str


def test_defaults_4_1():
    o = Arg(type=int)
    o.type = None
    assert o.type is str


def test_defaults_4_2():
    o = Arg(default=[])
    assert o.type is str


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(type=1.)
    assert str(e.value) == str(
        'Arg.type: Invalid type: float. '
        'Must be: type, None.')


def test_exceptions_1_1():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.type = 1
    assert str(e.value) == str(
        'Arg.type: Invalid type: int. '
        'Must be: type, None.')


def test_exceptions_2_0():
    o = Arg(default=[6])
    with pytest.raises(ValueError) as e:
        o.type = float
    assert str(e.value) == str(
        'Arg.type: Invalid value: float. '
        'Must match self.default: int.')


def test_exceptions_2_1():
    o = Arg(default=6)
    with pytest.raises(ValueError) as e:
        o.type = float
    assert str(e.value) == str(
        'Arg.type: Invalid value: float. '
        'Must match self.default: int.')
