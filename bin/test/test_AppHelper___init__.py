from .core import *


def test_description_0_0():
    o = AppHelper()
    assert o.sopt == 'h'
    assert o.lopt == 'help'
    assert o.help == 'Show the help text and exit.'


def test_description_0_1():
    o = AppHelper(
        sopt='s',
        lopt='lopt',
        help='Help.')
    assert o.sopt == 's'
    assert o.lopt == 'lopt'
    assert o.help == 'Help.'
