from .core import *


def test_description_1_0():
    o = Arg(default='2')
    assert o.default == '2'


def test_description_1_1():
    o = Arg()
    o.default = 3
    assert o.default == 3


def test_description_2_0():
    o = Arg(default=['1', '2'])
    assert o.default == ['1', '2']


def test_description_2_1():
    o = Arg()
    o.default = [3]
    assert o.default == [3]


def test_defaults_1_0():
    o = Arg(count=0, sopt='o')
    assert o.default is False


def test_defaults_1_1():
    o = Arg(sopt='o')
    o.count = 0
    assert o.default is False


def test_defaults_2_0():
    o = Arg(count='*')
    assert o.default == []
    o = Arg(count='~')
    assert o.default == []


def test_defaults_2_1():
    o = Arg()
    o.count = '*'
    assert o.default == []
    o = Arg()
    o.count = '~'
    assert o.default == []


def test_defaults_3_0():
    o = Arg()
    assert o.default is None


def test_defaults_3_1():
    o = Arg(default=[3, 4, 5])
    o.default = None
    assert o.count is 1
    assert o.default is None


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(count='+', default='abc')
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: list, None.')


def test_exceptions_1_1():
    o = Arg(count='+')
    with pytest.raises(TypeError) as e:
        o.default = 'abc'
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: list, None.')


def test_exceptions_2_0():
    with pytest.raises(TypeError) as e:
        Arg(count=1, default=['a', 'b', 'c'])
    assert str(e.value) == str(
        'Arg.default: Invalid type: list. '
        'Must be: object, None.')


def test_exceptions_2_1():
    o = Arg(count=1)
    with pytest.raises(TypeError) as e:
        o.default = ['a', 'b', 'c']
    assert str(e.value) == str(
        'Arg.default: Invalid type: list. '
        'Must be: object, None.')


def test_exceptions_3_0():
    with pytest.raises(TypeError) as e:
        Arg(type=int, default='3')
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: int, None.')


def test_exceptions_3_1():
    o = Arg(type=int)
    with pytest.raises(TypeError) as e:
        o.default = '1'
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: int, None.')


def test_exceptions_4_0():
    with pytest.raises(TypeError) as e:
        Arg(type=int, default=[1, '2', 3])
    assert str(e.value) == str(
        'Arg.default[1]: Invalid type: str. '
        'Must be: int.')


def test_exceptions_4_1():
    o = Arg(type=int)
    with pytest.raises(TypeError) as e:
        o.default = [1, '2', 3]
    assert str(e.value) == str(
        'Arg.default[1]: Invalid type: str. '
        'Must be: int.')


def test_exceptions_5_0():
    with pytest.raises(ValueError) as e:
        Arg(count=2, default=[1])
    assert str(e.value) == str(
        'Arg.default: Invalid value: len() is 1. '
        'Must match self.count: 2.')


def test_exceptions_5_1():
    o = Arg(count=2)
    with pytest.raises(ValueError) as e:
        o.default = [1]
    assert str(e.value) == str(
        'Arg.default: Invalid value: len() is 1. '
        'Must match self.count: 2.')


def test_exceptions_6_0():
    with pytest.raises(ValueError) as e:
        Arg(count='+', default=[])
    assert str(e.value) == str(
        'Arg.default: Invalid value: []. '
        'Must have at least one item, self.count is "+".')


def test_exceptions_6_1():
    o = Arg(count='+')
    with pytest.raises(ValueError) as e:
        o.default = []
    assert str(e.value) == str(
        'Arg.default: Invalid value: []. '
        'Must have at least one item, self.count is "+".')
