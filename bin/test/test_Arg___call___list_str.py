from .core import *


def test_return_1_0000():
    # Implicit default for *.
    o = Arg(count='*')
    assert o(None) == []


def test_return_1_0001():
    # Implicit default for +.
    o = Arg(count='+')
    assert o(None) == None


def test_return_1_0002():
    # Explicit default.
    o = Arg(count='~', default=['a', 'b'])
    assert o(None) == ['a', 'b']


def test_return_2_0000():
    # No conversion.
    o = Arg(count='*')
    assert o(['1', '2']) == ['1', '2']


def test_return_2_0001():
    # Conversion.
    o = Arg(count='*', type=int)
    assert o(['1', '2']) == [1, 2]


def test_exceptions_1_0000():
    # Restrict.
    o = Arg(
        name='ARG',
        count='*',
        choices=[1, 2, 3],
    )
    with pytest.raises(CallError) as e:
        o(['1', '4'])
    assert e.value.text == str(
        'Invalid value of argument ARG[1]: 4. '
        'Must be one of:'
        '\n * 1'
        '\n * 2'
        '\n * 3'
    )
    assert e.value.code == 1


def test_exceptions_1_0001():
    # No restrict.
    o = Arg(
        name='ARG',
        count='*',
        choices=[1, 2, 3],
        restrict=False,
    )
    assert o(['1', '4']) == ['1', '4']
