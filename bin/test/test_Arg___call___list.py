from .core import *


def test_return_1_0():
    o = Arg(sopt='o', append=True, type=int)
    assert o(['1', '2', '3']) == [1, 2, 3]


def test_return_1_1():
    o = Arg(sopt='o', count='?', append=True, type=int)
    assert o(['1', None, '2']) == [1, None, 2]


def test_return_1_2():
    o = Arg(sopt='o', count='?', append=True, default=5)
    assert o(['1', None, '2']) == [1, 5, 2]


def test_exceptions_1_0():
    with pytest.raises(CallError) as e:
        Arg(sopt='o', append=True, choices=[1, 2, 3])(['1', '4'])
    assert e.value.text == str(
        f'Invalid value of argument -o[1]: 4. '
        f'Must be one of:'
        f'\n * 1'
        f'\n * 2'
        f'\n * 3')
    assert e.value.code == 1


def test_exceptions_1_1():
    assert Arg(
        sopt='o',
        append=True,
        choices=[1, 2, 3],
        restrict=False)(['1', '4']) == ['1', '4']
