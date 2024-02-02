from .core import *


def test_defaults_1_0():
    o = Arg(count=1, sopt='o')
    assert o.single is True


def test_defaults_1_1():
    o = Arg(count='?', sopt='o')
    assert o.single is True


def test_defaults_2_0():
    o = Arg(count=0, sopt='o')
    assert o.single is False


def test_defaults_2_1():
    o = Arg(count=2, sopt='o')
    assert o.single is False


def test_defaults_2_2():
    o = Arg(count='*', sopt='o')
    assert o.single is False


def test_defaults_2_3():
    o = Arg(count='+', sopt='o')
    assert o.single is False


def test_defaults_2_4():
    o = Arg(count='~')
    assert o.single is False
