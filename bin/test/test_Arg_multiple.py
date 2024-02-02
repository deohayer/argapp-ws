from .core import *


def test_defaults_1_0():
    o = Arg(count=2, sopt='o')
    assert o.multiple is True


def test_defaults_1_1():
    o = Arg(count='*', sopt='o')
    assert o.multiple is True


def test_defaults_1_2():
    o = Arg(count='+', sopt='o')
    assert o.multiple is True


def test_defaults_1_3():
    o = Arg(count='~')
    assert o.multiple is True


def test_defaults_2_0():
    o = Arg(count=0, sopt='o')
    assert o.multiple is False


def test_defaults_2_1():
    o = Arg(count=1, sopt='o')
    assert o.multiple is False


def test_defaults_2_2():
    o = Arg(count='?', sopt='o')
    assert o.multiple is False
