from typing import Iterable

from .core import *
from argapp import _str


def test_0():
    # None.
    assert _str(None) == 'None'


def test_1():
    # bool.
    assert _str(True) == 'True'
    assert _str(False) == 'False'


def test_2():
    # int.
    assert _str(0) == '0'
    assert _str(1) == '1'


def test_3():
    # str.
    assert _str('') == '""'
    assert _str('abc') == '"abc"'


def test_4():
    # type.
    assert _str(str) == 'str'
    # NoneType is special.
    assert _str(type(None)) == 'None'


def test_5():
    # Other objects.
    assert _str(RuntimeError('Error')) == 'Error'


def test_6():
    # Iterable.
    assert _str(Iterable) == 'Iterable'
