from .core import *


def test_0_0000():
    # single.
    o = Arg()
    o.default = 3
    assert o.default == 3


def test_0_0001():
    # multiple.
    o = Arg()
    o.default = [3]
    assert o.default == [3]


def test_defaults_1_0000():
    o = Arg(sopt='o')
    o.count = 0
    assert o.default is False


def test_defaults_2_0000():
    o = Arg()
    o.count = '*'
    assert o.default == []


def test_defaults_2_0001():
    o = Arg()
    o.count = '~'
    assert o.default == []


def test_defaults_3_0000():
    o = Arg(default=1)
    o.default = None
    assert o.default is None


def test_exceptions_1_0000():
    o = Arg(count='+')
    with pytest.raises(TypeError) as e:
        o.default = 'abc'
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: list, None.')


def test_exceptions_2_0000():
    o = Arg(count=1)
    with pytest.raises(TypeError) as e:
        o.default = ['a', 'b', 'c']
    assert str(e.value) == str(
        'Arg.default: Invalid type: list. '
        'Must be: object, None.')


def test_exceptions_3_0000():
    o = Arg(type=int)
    with pytest.raises(TypeError) as e:
        o.default = '1'
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: int, None.')


def test_exceptions_4_0000():
    o = Arg(type=int)
    with pytest.raises(TypeError) as e:
        o.default = [1, '2', 3]
    assert str(e.value) == str(
        'Arg.default[1]: Invalid type: str. '
        'Must be: int.')


def test_exceptions_5_0000():
    o = Arg(count=2)
    with pytest.raises(ValueError) as e:
        o.default = [1]
    assert str(e.value) == str(
        'Arg.default: Invalid value: len() is 1. '
        'Must match self.count: 2.')


def test_exceptions_6_0000():
    o = Arg(count='+')
    with pytest.raises(ValueError) as e:
        o.default = []
    assert str(e.value) == str(
        'Arg.default: Invalid value: []. '
        'Must have at least one item, self.count is "+".')
