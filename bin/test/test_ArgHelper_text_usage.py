from .core import *


def test_returns_1_1_0():
    # sopt.
    arg = Arg(sopt='o', count=0)
    o = ArgHelper()
    assert o.text_usage(arg) == '-o'


def test_returns_1_2_0():
    # lopt.
    arg = Arg(lopt='option', count=0)
    o = ArgHelper()
    assert o.text_usage(arg) == '--option'


def test_returns_1_3_1_0():
    # int, flag.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count=0)
    o = ArgHelper()
    assert o.text_usage(arg) == '-o/--option'


def test_returns_1_3_1_1():
    # int, single positional.
    arg = Arg(
        name='OPT',
        count=1)
    o = ArgHelper()
    assert o.text_usage(arg) == 'OPT'


def test_returns_1_3_1_2():
    # int, single optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count=1)
    o = ArgHelper()
    assert o.text_usage(arg) == '-o/--option OPT'


def test_returns_1_3_1_3():
    # int, multiple positional.
    arg = Arg(
        name='OPT',
        count=2)
    o = ArgHelper()
    assert o.text_usage(arg) == 'OPT OPT'


def test_returns_1_3_1_4():
    # int, multiple optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count=2)
    o = ArgHelper()
    assert o.text_usage(arg) == '-o/--option OPT OPT'


def test_returns_1_3_2_0():
    # '?', positional.
    arg = Arg(
        name='OPT',
        count='?')
    o = ArgHelper()
    assert o.text_usage(arg) == '[OPT]'


def test_returns_1_3_2_1():
    # '?', optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count='?')
    o = ArgHelper()
    assert o.text_usage(arg) == '-o/--option [OPT]'


def test_returns_1_3_3_0():
    # '*', positional.
    arg = Arg(
        name='OPT',
        count='*')
    o = ArgHelper()
    assert o.text_usage(arg) == '[OPT...]'


def test_returns_1_3_3_1():
    # '*', optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count='*')
    o = ArgHelper()
    assert o.text_usage(arg) == '-o/--option [OPT...]'


def test_returns_1_3_4_0():
    # '+', positional.
    arg = Arg(
        name='OPT',
        count='+')
    o = ArgHelper()
    assert o.text_usage(arg) == 'OPT [OPT...]'


def test_returns_1_3_4_1():
    # '+', optional.
    arg = Arg(
        name='OPT',
        sopt='o',
        lopt='option',
        count='+')
    o = ArgHelper()
    assert o.text_usage(arg) == '-o/--option OPT [OPT...]'


def test_returns_1_3_5_0():
    # '~'.
    arg = Arg(
        name='OPT',
        count='~')
    o = ArgHelper()
    assert o.text_usage(arg) == '[OPT]...'
