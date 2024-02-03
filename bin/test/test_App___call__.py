from .core import *


def test_description_1_0():
    o = App()
    assert o({}, [o]) is None
