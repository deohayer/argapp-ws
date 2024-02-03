from .core import *


def test_returns_1_0():
    assert AppHelper().section_apps('Title', []) == ''


def test_returns_2_0():
    a1 = App('a')
    a2 = App('application', 'help')
    a3 = App('app', 'h\ne\nl\np')
    act = AppHelper().section_apps(
        'Title',
        [a1, a2, a3])
    exp = str(
        'Title:\n'
        ' * a\n'
        ' * application - help\n'
        ' * app         - h\n'
        '                 e\n'
        '                 l\n'
        '                 p')
    assert act == exp


def test_returns_2_1():
    a1 = App('a')
    a2 = App('application', 'help')
    a3 = App('app', 'h\ne\nl\np')
    act = AppHelper().section_apps(
        '',
        [a1, a2, a3])
    exp = str(
        ' * a\n'
        ' * application - help\n'
        ' * app         - h\n'
        '                 e\n'
        '                 l\n'
        '                 p')
    assert act == exp
