from .core import *


def test_return_1_0000():
    # Conversion.
    o = Arg(
        sopt='o',
        append=True,
        type=int,
    )
    assert o(['1', '2', '3']) == [1, 2, 3]


def test_return_1_0001():
    # Misc, no default.
    o = Arg(
        sopt='o',
        count='?',
        append=True,
        type=int,
    )
    assert o(['1', None, '2']) == [1, None, 2]


def test_return_1_0002():
    # Misc, default.
    o = Arg(
        sopt='o',
        count='?',
        append=True,
        default=5,
    )
    assert o(['1', None, '2']) == [1, 5, 2]


def test_exceptions_1_0000():
    # Restrict.
    o = Arg(
        sopt='o',
        append=True,
        choices=[1, 2, 3],
    )
    with pytest.raises(CallError) as e:
        o(['1', '4'])
    assert e.value.text == str(
        'Invalid value of argument -o[1]: 4. '
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
        append=True,
        choices=[1, 2, 3],
        restrict=False,
    )
    assert o(['1', '4']) == ['1', '4']
