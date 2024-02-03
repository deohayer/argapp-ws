from .core import *


def test_return_1_0():
    o = Arg(sopt='o', count='*', append=True)
    assert o([]) == []


def test_return_1_1():
    o = Arg(sopt='o', count='*', append=True)
    assert o([None]) == [[]]


def test_return_1_2():
    o = Arg(sopt='o', count='*', append=True, default=[2, 3])
    assert o([['1'], None, ['4', '5']]) == [[1], [2, 3], [4, 5]]


def test_exceptions_1_0():
    with pytest.raises(CallError) as e:
        Arg(sopt='o',
            count='*',
            append=True,
            choices=[1, 2, 3])([['2', '3'], None, ['4', '1']])
    assert e.value.text == str(
        f'Invalid value of argument -o[2][0]: 4. '
        f'Must be one of:'
        f'\n * 1'
        f'\n * 2'
        f'\n * 3')
    assert e.value.code == 1


def test_exceptions_1_1():
    assert Arg(
        sopt='o',
        count='*',
        append=True,
        choices=[1, 2, 3],
        restrict=False)([['2', '3'], None, ['4', '1']]) == [['2', '3'], [], ['4', '1']]
