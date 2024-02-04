from .core import *


def test_returns_1_0000():
    assert AppHelper().section_apps('Title', []) == ''


def test_returns_2_0000():
    # Title.
    title = 'Title'
    apps = [
        App('a'),
        App('application', 'help'),
        App('app', 'h\ne\nl\np'),
    ]
    assert AppHelper().section_apps(title, apps) == str(
        'Title:\n'
        '  a\n'
        '  application    help\n'
        '  app            h\n'
        '                 e\n'
        '                 l\n'
        '                 p'
    )


def test_returns_2_0001():
    # No title.
    title = ''
    apps = [
        App('a'),
        App('application', 'help'),
        App('app', 'h\ne\nl\np'),
    ]
    assert AppHelper().section_apps(title, apps) == str(
        '  a\n'
        '  application    help\n'
        '  app            h\n'
        '                 e\n'
        '                 l\n'
        '                 p'
    )
