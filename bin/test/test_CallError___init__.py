from .core import *


def test_description_0_0000():
    o = CallError()
    assert o.text == ''
    assert o.code == 1


def test_description_0_0001():
    o = CallError('Error', 1)
    assert o.text == 'Error'
    assert o.code == 1
