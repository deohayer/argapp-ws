from .core import *


def test_return_1_0000():
    # Explicit default.
    o = Arg(default=5)
    assert o(None) == 5


def test_return_1_0001():
    # Implicit default.
    o = Arg()
    assert o(None) is None


def test_return_2_0000():
    # No conversion.
    o = Arg()
    assert o('value') == 'value'


def test_return_2_0001():
    # Conversion.
    o = Arg(type=int)
    assert o('10') == 10


def test_exceptions_1_0000():
    # Restrict.
    o = Arg(
        name='ARG',
        choices=[1, 2, 3],
    )
    with pytest.raises(CallError) as e:
        o('4')
    assert e.value.text == str(
        'Invalid value of argument ARG: 4. '
        'Must be one of:'
        '\n * 1'
        '\n * 2'
        '\n * 3')
    assert e.value.code == 1


def test_exceptions_1_0001():
    # No restrict.
    o = Arg(
        name='ARG',
        choices=[1, 2, 3],
        restrict=False,
    )
    assert o('4') == '4'
