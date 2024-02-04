from .core import *


def test_returns_1_0000():
    assert AppHelper().section_apps('Title', []) == ''


def test_returns_2_0000():
    # Title.
    title = 'Title'
    args = [
        Arg(name='ARGUMENT', help='help'),
        Arg(lopt='opt', help='h\ne\nl\np'),
    ]
    assert AppHelper().section_args(title, args) == str(
        'Title:\n'
        '  ARGUMENT     help\n'
        '  --opt OPT    h\n'
        '               e\n'
        '               l\n'
        '               p'
    )


def test_returns_2_0001():
    # No title.
    title = ''
    args = [
        Arg(name='ARGUMENT', help='help'),
        Arg(lopt='opt', help='h\ne\nl\np'),
    ]
    assert AppHelper().section_args(title, args) == str(
        '  ARGUMENT     help\n'
        '  --opt OPT    h\n'
        '               e\n'
        '               l\n'
        '               p'
    )
