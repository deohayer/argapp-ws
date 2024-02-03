from .core import *


def test_return_1_0():
    o = Arg(default=5)
    assert o(None) == 5


def test_return_1_1():
    o = Arg()
    assert o(None) is None


def test_return_2_0():
    o = Arg()
    assert o('value') == 'value'


def test_return_2_1():
    o = Arg(type=int)
    assert o('10') == 10


def test_exceptions_1_0():
    with pytest.raises(CallError) as e:
        Arg(name='ARG', choices=[1, 2, 3])('4')
    assert e.value.text == str(
        f'Invalid value of argument ARG: 4. '
        f'Must be one of:'
        f'\n * 1'
        f'\n * 2'
        f'\n * 3')
    assert e.value.code == 1


def test_exceptions_1_1():
    assert Arg(choices=[1, 2, 3], restrict=False)('4') == '4'
