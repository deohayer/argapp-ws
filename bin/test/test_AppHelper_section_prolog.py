from .core import *


def test_returns_1_0():
    assert AppHelper().section_prolog('Title', App()) == ''


def test_returns_2_0():
    act = AppHelper().section_prolog(
        'Title',
        App(prolog='This is prolog.'))
    exp = str(
        'Title:\n'
        'This is prolog.')
    assert act == exp


def test_returns_2_1():
    act = AppHelper().section_prolog(
        '',
        App(prolog='This is prolog.'))
    exp = 'This is prolog.'
    assert act == exp
