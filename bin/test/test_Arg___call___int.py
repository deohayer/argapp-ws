from .core import *


def test_return_1_0():
    o = Arg(sopt='o', count=0, append=True)
    assert o(0) is 0


def test_return_1_1():
    o = Arg(sopt='o', count=0, append=True)
    assert o(2) is 2
