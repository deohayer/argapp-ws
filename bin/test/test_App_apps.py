from .core import *


def test_defaults_1_0():
    o = App()
    assert o.apps == []
