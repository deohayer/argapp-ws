from .core import *


def test_defaults_1_0000():
    # sopt.
    o = Arg(sopt='s')
    assert o.optional is True


def test_defaults_1_0001():
    # lopt.
    o = Arg(lopt='lopt')
    assert o.optional is True


def test_defaults_2_0000():
    o = Arg()
    assert o.optional is False
