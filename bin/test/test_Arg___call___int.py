from .core import *


def test_return_1_0000():
    # Zero.
    o = Arg(sopt='o', count=0, append=True)
    assert o(0) is 0


def test_return_1_0001():
    # Normal value.
    o = Arg(sopt='o', count=0, append=True)
    assert o(2) is 2
