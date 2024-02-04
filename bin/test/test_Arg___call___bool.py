from .core import *


def test_return_1_0000():
    # Normal.
    o = Arg(sopt='o', count=0)
    assert o(False) is False


def test_return_1_0001():
    # Flipped.
    o = Arg(sopt='o', count=0, default=True)
    assert o(False) is True


def test_return_2_0000():
    # Normal.
    o = Arg(sopt='o', count=0)
    assert o(True) is True


def test_return_2_0001():
    # Flipped.
    o = Arg(sopt='o', count=0, default=True)
    assert o(True) is False
