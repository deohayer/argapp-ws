from .core import *


def test_returns_1_0():
    # default, choices and help.
    arg = Arg(
        help='An argument.',
        count='?',
        default=1,
        choices=[1, 2, 3])
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'An argument.\n'
        'Default: 1\n'
        'Allowed values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3')


def test_returns_1_1():
    # Flag.
    arg = Arg(
        sopt='o',
        help='An argument.',
        count=0,
        default=True,
        choices=['True', 'False'])
    o = ArgHelper()
    assert o.text_help(arg) == 'An argument.'


def test_returns_1_1_0():
    # default is None.
    arg = Arg(
        count='?',
        default=None)
    o = ArgHelper()
    assert o.text_help(arg) == ''


def test_returns_1_1_1():
    # default is an empty array.
    arg = Arg(
        count='*',
        default=[])
    o = ArgHelper()
    assert o.text_help(arg) == ''


def test_returns_1_1_2():
    # default is an empty string.
    arg = Arg(
        count='?',
        default='')
    o = ArgHelper()
    assert o.text_help(arg) == 'Default: ""'


def test_returns_1_1_3():
    # default is a single value.
    arg = Arg(
        count='?',
        default='value')
    o = ArgHelper()
    assert o.text_help(arg) == 'Default: value'


def test_returns_1_1_4():
    # default is a list.
    arg = Arg(
        help='An argument.',
        count='*',
        default=['value1', '', 'value2'])
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'An argument.\n'
        'Default: value1 "" value2')


def test_returns_1_1_5():
    # default is disabled.
    arg = Arg(
        count='?',
        default='value')
    o = ArgHelper(default=False)
    assert o.text_help(arg) == ''


def test_returns_1_1_6():
    # default and help.
    arg = Arg(
        help='An argument.',
        count='?',
        default='value')
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'An argument.\n'
        'Default: value')


def test_returns_1_2_0():
    # choices restricted.
    arg = Arg(
        choices=[1, 2, 3])
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'Allowed values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3')


def test_returns_1_2_1():
    # choices not restricted.
    arg = Arg(
        choices=[1, 2, 3],
        restrict=False)
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'Possible values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3')


def test_returns_1_2_2():
    # choices and help.
    arg = Arg(
        help='An argument.',
        choices=[1, 2, 3])
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'An argument.\n'
        'Allowed values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3')


def test_returns_1_2_3():
    # choices disabled.
    arg = Arg(
        help='An argument.',
        choices=[1, 2, 3])
    o = ArgHelper(choices=False)
    assert o.text_help(arg) == 'An argument.'


def test_returns_1_2_4():
    # choices with different sizes and helps.
    arg = Arg(
        choices={
            'v1': '',
            'value2': 'help',
            'val3': 'h\ne\nl\np',
        })
    o = ArgHelper()
    assert o.text_help(arg) == str(
        'Allowed values:\n'
        ' * v1\n'
        ' * value2 - help\n'
        ' * val3   - h\n'
        '            e\n'
        '            l\n'
        '            p')
