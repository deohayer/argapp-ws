from .core import *


def test_return_1_0000():
    # Empty.
    o = Arg(sopt='o', count='*', append=True)
    assert o([]) == []


def test_return_1_0001():
    # None.
    o = Arg(sopt='o', count='*', append=True)
    assert o([None]) == [[]]


def test_return_1_0002():
    # Misc.
    raw = [
        ['1'],
        None,
        ['4', '5'],
    ]
    parsed = [
        [1],
        [2, 3],
        [4, 5],
    ]
    o = Arg(
        sopt='o',
        count='*',
        append=True,
        default=[2, 3],
    )
    assert o(raw) == parsed


def test_exceptions_1_0000():
    # Restrict.
    o = Arg(
        sopt='o',
        count='*',
        append=True,
        choices=[1, 2, 3],
    )
    raw = [
        ['2', '3'],
        None,
        ['4', '1'],
    ]
    with pytest.raises(CallError) as e:
        o(raw)
    assert e.value.text == str(
        'Invalid value of argument -o[2][0]: 4. '
        'Must be one of:'
        '\n * 1'
        '\n * 2'
        '\n * 3'
    )
    assert e.value.code == 1


def test_exceptions_1_0001():
    # No restrict.
    o = Arg(
        sopt='o',
        count='*',
        append=True,
        choices=[1, 2, 3],
        restrict=False,
    )
    raw = [
        ['2', '3'],
        None,
        ['4', '1'],
    ]
    parsed = [
        ['2', '3'],
        [],
        ['4', '1'],
    ]
    assert o(raw) == parsed
