from .core import *


def test_return_1_0():
    o = Arg(count='*')
    assert o(None) == []


def test_return_1_1():
    o = Arg(count='+')
    assert o(None) == None


def test_return_1_2():
    o = Arg(count='~', default=['a', 'b'])
    assert o(None) == ['a', 'b']


def test_return_2_0():
    o = Arg(count='*')
    assert o(['1', '2']) == ['1', '2']


def test_return_2_1():
    o = Arg(count='*', type=int)
    assert o(['1', '2']) == [1, 2]


def test_exceptions_1_0():
    with pytest.raises(CallError) as e:
        Arg(name='ARG', count='*', choices=[1, 2, 3])(['1', '4'])
    assert e.value.text == str(
        f'Invalid value of argument ARG[1]: 4. '
        f'Must be one of:'
        f'\n * 1'
        f'\n * 2'
        f'\n * 3')
    assert e.value.code == 1


def test_exceptions_1_1():
    assert Arg(
        name='ARG',
        count='*',
        choices=[1, 2, 3],
        restrict=False)(['1', '4']) == ['1', '4']
