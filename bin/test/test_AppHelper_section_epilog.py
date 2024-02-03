from .core import *


def test_returns_1_0():
    assert AppHelper().section_epilog('Title', App()) == ''


def test_returns_2_0():
    act = AppHelper().section_epilog(
        'Title',
        App(epilog='This is epilog.'))
    exp = str(
        'Title:\n'
        'This is epilog.')
    assert act == exp


def test_returns_2_1():
    act = AppHelper().section_epilog(
        '',
        App(epilog='This is epilog.'))
    exp = 'This is epilog.'
    assert act == exp
