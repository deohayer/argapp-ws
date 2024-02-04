from .core import *


def test_returns_1_1_0000():
    # sopt.
    arg = Arg(sopt='o', count=0)
    assert ArgHelper().text_usage(arg) == '-o'


def test_returns_1_2_0000():
    # lopt.
    arg = Arg(lopt='option', count=0)
    assert ArgHelper().text_usage(arg) == '--option'


def test_returns_1_3_1_0000():
    # int, flag.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count=0,
    )
    assert ArgHelper().text_usage(arg) == '-o/--option'


def test_returns_1_3_1_0001():
    # int, single positional.
    arg = Arg(
        name='OPT',
        count=1,
    )
    assert ArgHelper().text_usage(arg) == 'OPT'


def test_returns_1_3_1_0002():
    # int, single optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count=1,
    )
    assert ArgHelper().text_usage(arg) == '-o/--option OPT'


def test_returns_1_3_1_0003():
    # int, multiple positional.
    arg = Arg(
        name='OPT',
        count=2,
    )
    assert ArgHelper().text_usage(arg) == 'OPT OPT'


def test_returns_1_3_1_0004():
    # int, multiple optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count=2,
    )
    assert ArgHelper().text_usage(arg) == '-o/--option OPT OPT'


def test_returns_1_3_2_0000():
    # '?', positional.
    arg = Arg(
        name='OPT',
        count='?',
    )
    assert ArgHelper().text_usage(arg) == '[OPT]'


def test_returns_1_3_2_0001():
    # '?', optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count='?',
    )
    assert ArgHelper().text_usage(arg) == '-o/--option [OPT]'


def test_returns_1_3_3_0000():
    # '*', positional.
    arg = Arg(
        name='OPT',
        count='*',
    )
    assert ArgHelper().text_usage(arg) == '[OPT...]'


def test_returns_1_3_3_0001():
    # '*', optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count='*',
    )
    assert ArgHelper().text_usage(arg) == '-o/--option [OPT...]'


def test_returns_1_3_4_0000():
    # '+', positional.
    arg = Arg(
        name='OPT',
        count='+',
    )
    assert ArgHelper().text_usage(arg) == 'OPT [OPT...]'


def test_returns_1_3_4_0001():
    # '+', optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count='+',
    )
    assert ArgHelper().text_usage(arg) == '-o/--option OPT [OPT...]'


def test_returns_1_3_5_0000():
    # '~'.
    arg = Arg(
        name='OPT',
        count='~',
    )
    assert ArgHelper().text_usage(arg) == '[OPT]...'
