from .core import *


def test_defaults_1_0000():
    o = Arg(count=1, sopt='o')
    assert o.single is True


def test_defaults_1_0001():
    o = Arg(count='?', sopt='o')
    assert o.single is True


def test_defaults_2_0000():
    o = Arg(count=0, sopt='o')
    assert o.single is False


def test_defaults_2_0001():
    o = Arg(count=2, sopt='o')
    assert o.single is False


def test_defaults_2_0002():
    o = Arg(count='*', sopt='o')
    assert o.single is False


def test_defaults_2_0003():
    o = Arg(count='+', sopt='o')
    assert o.single is False


def test_defaults_2_0004():
    o = Arg(count='~')
    assert o.single is False
