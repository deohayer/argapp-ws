from .core import *


def test_description_1_0():
    o = Arg(sopt='o', count=0)
    assert o.count == 0


def test_description_1_1():
    o = Arg(sopt='o')
    o.count = 0
    assert o.count == 0


def test_description_2_0():
    o = Arg(count=1)
    assert o.count == 1


def test_description_2_1():
    o = Arg()
    o.count = 1
    assert o.count == 1


def test_description_2_2():
    o = Arg(sopt='o', count=1)
    assert o.count == 1


def test_description_2_3():
    o = Arg(sopt='o')
    o.count = 1
    assert o.count == 1


def test_description_3_0():
    o = Arg(count=2)
    assert o.count == 2


def test_description_3_1():
    o = Arg()
    o.count = 2
    assert o.count == 2


def test_description_3_2():
    o = Arg(sopt='o', count=2)
    assert o.count == 2


def test_description_3_3():
    o = Arg(sopt='o')
    o.count = 2
    assert o.count == 2


def test_description_4_0():
    o = Arg(count='?')
    assert o.count == '?'


def test_description_4_1():
    o = Arg()
    o.count = '?'
    assert o.count == '?'


def test_description_4_2():
    o = Arg(sopt='o', count='?')
    assert o.count == '?'


def test_description_4_3():
    o = Arg(sopt='o')
    o.count = '?'
    assert o.count == '?'


def test_description_4_0():
    o = Arg(count='*')
    assert o.count == '*'


def test_description_5_1():
    o = Arg()
    o.count = '*'
    assert o.count == '*'


def test_description_5_2():
    o = Arg(sopt='o', count='*')
    assert o.count == '*'


def test_description_5_3():
    o = Arg(sopt='o')
    o.count = '*'
    assert o.count == '*'


def test_description_6_0():
    o = Arg(count='+')
    assert o.count == '+'


def test_description_6_1():
    o = Arg()
    o.count = '+'
    assert o.count == '+'


def test_description_6_2():
    o = Arg(sopt='o', count='+')
    assert o.count == '+'


def test_description_6_3():
    o = Arg(sopt='o')
    o.count = '+'
    assert o.count == '+'


def test_description_7_0():
    o = Arg(count='~')
    assert o.count == '~'


def test_description_7_1():
    o = Arg()
    o.count = '~'
    assert o.count == '~'


def test_defaults_1_0():
    o = Arg(default=[])
    assert o.count == '*'


def test_defaults_1_1():
    o = Arg()
    o.default = []
    assert o.count == '*'


def test_defaults_1_2():
    o = Arg(default=[1], count='+')
    assert o.count == '+'
    o.count = None
    assert o.count == '*'


def test_defaults_2_0():
    o = Arg()
    assert o.count == 1


def test_defaults_2_1():
    o = Arg(count=5)
    o.count = None
    assert o.count == 1


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(count=1.)
    assert str(e.value) == str(
        'Arg.count: Invalid type: float. '
        'Must be: int, str, None.')


def test_exceptions_1_1():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.count = []
    assert str(e.value) == str(
        'Arg.count: Invalid type: list. '
        'Must be: int, str, None.')


def test_exceptions_2_0():
    with pytest.raises(ValueError) as e:
        Arg(count=-1)
    assert str(e.value) == str(
        'Arg.count: Invalid value: -1. '
        'Must be positive for positional.')


def test_exceptions_2_1():
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.count = -3
    assert str(e.value) == str(
        'Arg.count: Invalid value: -3. '
        'Must be positive for positional.')


def test_exceptions_2_2():
    with pytest.raises(ValueError) as e:
        Arg(count=-1, sopt='o')
    assert str(e.value) == str(
        'Arg.count: Invalid value: -1. '
        'Must be non-negative for optional.')


def test_exceptions_2_3():
    o = Arg(sopt='o')
    with pytest.raises(ValueError) as e:
        o.count = -3
    assert str(e.value) == str(
        'Arg.count: Invalid value: -3. '
        'Must be non-negative for optional.')


def test_exceptions_3_0():
    with pytest.raises(ValueError) as e:
        Arg(count='$')
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*", "+" or "~" for positional.')


def test_exceptions_3_1():
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.count = '$'
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*", "+" or "~" for positional.')


def test_exceptions_3_2():
    with pytest.raises(ValueError) as e:
        Arg(count='$', sopt='o')
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*" or "+" for optional.')


def test_exceptions_3_3():
    o = Arg(sopt='o')
    with pytest.raises(ValueError) as e:
        o.count = "$"
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*" or "+" for optional.')


def test_exceptions_4_0():
    with pytest.raises(ValueError) as e:
        Arg(count=0)
    assert str(e.value) == str(
        'Arg.count: Invalid value: 0. '
        'Must be positive for positional.')


def test_exceptions_4_1():
    o = Arg()
    with pytest.raises(ValueError) as e:
        o.count = 0
    assert str(e.value) == str(
        'Arg.count: Invalid value: 0. '
        'Must be positive for positional.')


def test_exceptions_5_0():
    with pytest.raises(ValueError) as e:
        Arg(count='~', sopt='o')
    assert str(e.value) == str(
        'Arg.count: Invalid value: "~". '
        'Must be "?", "*" or "+" for optional.')


def test_exceptions_5_1():
    o = Arg(sopt='o')
    with pytest.raises(ValueError) as e:
        o.count = "~"
    assert str(e.value) == str(
        'Arg.count: Invalid value: "~". '
        'Must be "?", "*" or "+" for optional.')


def test_exceptions_6_0():
    o = Arg(default=[])
    with pytest.raises(ValueError) as e:
        o.count = '+'
    assert str(e.value) == str(
        'Arg.count: Invalid value: "+". '
        'Must allow zero values, self.default is empty.')


def test_exceptions_7_0():
    o = Arg(default=[1, 2, 3])
    with pytest.raises(ValueError) as e:
        o.count = 2
    assert str(e.value) == str(
        'Arg.count: Invalid value: 2. '
        'Must match the number of values in self.default: 3.')
