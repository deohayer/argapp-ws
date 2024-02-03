from .core import *


def test_return_1_0():
    o = Arg(sopt='o', count=0)
    assert o(False) is False


def test_return_1_1():
    o = Arg(sopt='o', count=0, default=True)
    assert o(False) is True


def test_return_2_0():
    o = Arg(sopt='o', count=0)
    assert o(True) is True


def test_return_2_1():
    o = Arg(sopt='o', count=0, default=True)
    assert o(True) is False
