from .core import *


def test_returns_1_0000():
    # default, choices and help.
    arg = Arg(
        help='An argument.',
        count='?',
        default=1,
        choices=[1, 2, 3],
    )
    assert ArgHelper().text_help(arg) == str(
        'An argument.\n'
        'Default: 1\n'
        'Allowed values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3'
    )


def test_returns_1_0001():
    # Flag.
    arg = Arg(
        sopt='o',
        help='An argument.',
        count=0,
        default=True,
        choices=['True', 'False'],
    )
    assert ArgHelper().text_help(arg) == 'An argument.'


def test_returns_1_1_0000():
    # default is None.
    arg = Arg(
        count='?',
        default=None,
    )
    assert ArgHelper().text_help(arg) == ''


def test_returns_1_1_0001():
    # default is an empty array.
    arg = Arg(
        count='*',
        default=[],
    )
    assert ArgHelper().text_help(arg) == ''


def test_returns_1_1_0002():
    # default is an empty string.
    arg = Arg(
        count='?',
        default='',
    )
    o = ArgHelper()
    assert ArgHelper().text_help(arg) == 'Default: ""'


def test_returns_1_1_0003():
    # default is a single value.
    arg = Arg(
        count='?',
        default='value',
    )
    assert ArgHelper().text_help(arg) == 'Default: value'


def test_returns_1_1_0004():
    # default is a list.
    arg = Arg(
        help='An argument.',
        count='*',
        default=['value1', '', 'value2'],
    )
    assert ArgHelper().text_help(arg) == str(
        'An argument.\n'
        'Default: value1 "" value2'
    )


def test_returns_1_1_0005():
    # default is disabled.
    arg = Arg(
        count='?',
        default='value',
    )
    assert ArgHelper(default=False).text_help(arg) == ''


def test_returns_1_1_0006():
    # default and help.
    arg = Arg(
        help='An argument.',
        count='?',
        default='value',
    )
    assert ArgHelper().text_help(arg) == str(
        'An argument.\n'
        'Default: value'
    )


def test_returns_1_2_0000():
    # choices restricted.
    arg = Arg(choices=[1, 2, 3])
    assert ArgHelper().text_help(arg) == str(
        'Allowed values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3'
    )


def test_returns_1_2_0001():
    # choices not restricted.
    arg = Arg(
        choices=[1, 2, 3],
        restrict=False,
    )
    assert ArgHelper().text_help(arg) == str(
        'Possible values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3'
    )


def test_returns_1_2_0002():
    # choices and help.
    arg = Arg(
        help='An argument.',
        choices=[1, 2, 3],
    )
    assert ArgHelper().text_help(arg) == str(
        'An argument.\n'
        'Allowed values:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3'
    )


def test_returns_1_2_0003():
    # choices is disabled.
    arg = Arg(choices=[1, 2, 3])
    assert ArgHelper(choices=False).text_help(arg) == ''


def test_returns_1_2_0004():
    # choices with different sizes and helps.
    arg = Arg(
        choices={
            'v1': '',
            'value2': 'help',
            'val3': 'h\ne\nl\np',
        },
    )
    assert ArgHelper().text_help(arg) == str(
        'Allowed values:\n'
        ' * v1\n'
        ' * value2 - help\n'
        ' * val3   - h\n'
        '            e\n'
        '            l\n'
        '            p'
    )
