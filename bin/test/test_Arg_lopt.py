from .core import *


def test_0_0000():
    o = Arg()
    o.lopt = 'lopt'
    assert o.lopt == 'lopt'


def test_defaults_1_0000():
    o = Arg(lopt='lopt')
    o.lopt = None
    assert o.lopt == ''


def test_exceptions_1_0000():
    # Assignment.
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.lopt = 1.
    assert str(e.value) == str(
        'Arg.lopt: Invalid type: float. '
        'Must be: str, None.'
    )
