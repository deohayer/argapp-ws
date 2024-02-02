from .core import *


def test_description_1_0():
    o = Arg(choices={
        'item1': 'help1',
        'item2': 'help2',
    })
    assert o.choices == {
        'item1': 'help1',
        'item2': 'help2',
    }


def test_description_1_1():
    o = Arg()
    o.choices = {
        'item1': 'help1',
        'item2': 'help2',
    }
    assert o.choices == {
        'item1': 'help1',
        'item2': 'help2',
    }


def test_description_1_2():
    o = Arg(choices=['item1', 'item2'])
    assert o.choices == {
        'item1': '',
        'item2': '',
    }


def test_description_1_3():
    o = Arg()
    o.choices = ['item1', 'item2']
    assert o.choices == {
        'item1': '',
        'item2': '',
    }


def test_description_1_4():
    o = Arg(choices=[1, 2])
    assert o.choices == {
        '1': '',
        '2': '',
    }


def test_description_1_5():
    o = Arg(choices={1: 1, 2: 2})
    assert o.choices == {
        '1': '1',
        '2': '2',
    }


def test_defaults_1_0():
    o = Arg()
    assert o.choices == {}


def test_defaults_1_1():
    o = Arg(choices={
        'item1': 'help1',
        'item2': 'help2',
    })
    o.choices = None
    assert o.choices == {}


def test_exceptions_1_0():
    with pytest.raises(TypeError) as e:
        Arg(choices=1.)
    assert str(e.value) == str(
        'Arg.choices: Invalid type: float. '
        'Must be: Iterable, None.')


def test_exceptions_1_1():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.choices = 1.
    assert str(e.value) == str(
        'Arg.choices: Invalid type: float. '
        'Must be: Iterable, None.')
