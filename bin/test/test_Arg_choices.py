from .core import *


def test_0_0000():
    # dict[str, str].
    o = Arg()
    o.choices = {
        'item1': 'help1',
        'item2': 'help2',
    }
    assert o.choices == {
        'item1': 'help1',
        'item2': 'help2',
    }


def test_0_0001():
    # list[str].
    o = Arg()
    o.choices = ['item1', 'item2']
    assert o.choices == {
        'item1': '',
        'item2': '',
    }


def test_0_0002():
    # list[int].
    o = Arg()
    o.choices = [1, 2]
    assert o.choices == {
        '1': '',
        '2': '',
    }


def test_description_1_5():
    # dict[int, int].
    o = Arg()
    o.choices = {
        1: 1,
        2: 2,
    }
    assert o.choices == {
        '1': '1',
        '2': '2',
    }


def test_defaults_1_0000():
    o = Arg(choices={
        'item1': 'help1',
        'item2': 'help2',
    })
    o.choices = None
    assert o.choices == {}


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.choices = 1.
    assert str(e.value) == str(
        'Arg.choices: Invalid type: float. '
        'Must be: Iterable, None.')
