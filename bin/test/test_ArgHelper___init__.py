from .core import *


def test_description_1_0():
    o = ArgHelper()
    assert o.choices is True
    assert o.default is True


def test_description_1_1():
    o = ArgHelper(
        default=False,
        choices=False)
    assert o.choices is False
    assert o.default is False
