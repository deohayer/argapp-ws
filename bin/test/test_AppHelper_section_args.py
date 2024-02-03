from .core import *


def test_returns_1_0():
    assert AppHelper().section_apps('Title', []) == ''


def test_returns_2_0():
    arg = Arg(name='ARGUMENT', help='help')
    opt = Arg(lopt='opt', help='h\ne\nl\np')
    act = AppHelper().section_args(
        'Title',
        [arg, opt])
    exp = str(
        'Title:\n'
        '  ARGUMENT     help\n'
        '  --opt OPT    h\n'
        '               e\n'
        '               l\n'
        '               p')
    assert act == exp


def test_returns_2_1():
    arg = Arg(name='ARGUMENT', help='help')
    opt = Arg(lopt='opt', help='h\ne\nl\np')
    act = AppHelper().section_args(
        '',
        [arg, opt])
    exp = str(
        '  ARGUMENT     help\n'
        '  --opt OPT    h\n'
        '               e\n'
        '               l\n'
        '               p')
    assert act == exp
