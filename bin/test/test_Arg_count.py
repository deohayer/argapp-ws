from .core import *


def test_1_0000():
    o = Arg(sopt='o')
    o.count = 0
    assert o.count == 0


def test_2_0000():
    o = Arg()
    o.count = 1
    assert o.count == 1


def test_3_0000():
    o = Arg()
    o.count = 2
    assert o.count == 2


def test_4_0000():
    o = Arg()
    o.count = '?'
    assert o.count == '?'


def test_5_0000():
    o = Arg()
    o.count = '*'
    assert o.count == '*'


def test_6_0000():
    o = Arg()
    o.count = '+'
    assert o.count == '+'


def test_7_0000():
    o = Arg()
    o.count = '~'
    assert o.count == '~'


def test_defaults_1_0000():
    o = Arg(count='+', default=[1])
    o.count = None
    assert o.count == '*'


def test_defaults_2_0000():
    o = Arg(count=5)
    o.count = None
    assert o.count == 1


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.count = 1.
    assert str(e.value) == str(
        'Arg.count: Invalid type: float. '
        'Must be: int, str, None.')


def test_exceptions_2_0000():
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.count = -3
    assert str(e.value) == str(
        'Arg.count: Invalid value: -3. '
        'Must be positive for positional.')


def test_exceptions_2_0001():
    o = Arg(sopt='o')
    with pytest.raises(ValueError) as e:
        o.count = -3
    assert str(e.value) == str(
        'Arg.count: Invalid value: -3. '
        'Must be non-negative for optional.')


def test_exceptions_3_0000():
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.count = '$'
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*", "+" or "~" for positional.')


def test_exceptions_3_0001():
    o = Arg(sopt='o')
    with pytest.raises(ValueError) as e:
        o.count = '$'
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*" or "+" for optional.')


def test_exceptions_4_0000():
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.count = 0
    assert str(e.value) == str(
        'Arg.count: Invalid value: 0. '
        'Must be positive for positional.')


def test_exceptions_5_0000():
    o = Arg(sopt='o')
    with pytest.raises(ValueError) as e:
        o.count = '~'
    assert str(e.value) == str(
        'Arg.count: Invalid value: "~". '
        'Must be "?", "*" or "+" for optional.')


def test_exceptions_6_0000():
    o = Arg(default=[])
    with pytest.raises(ValueError) as e:
        o.count = '+'
    assert str(e.value) == str(
        'Arg.count: Invalid value: "+". '
        'Must allow zero values, self.default is empty.')


def test_exceptions_7_0000():
    o = Arg(default=[1, 2, 3])
    with pytest.raises(ValueError) as e:
        o.count = 2
    assert str(e.value) == str(
        'Arg.count: Invalid value: 2. '
        'Must match the number of values in self.default: 3.')
