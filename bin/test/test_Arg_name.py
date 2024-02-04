from .core import *


def test_0_0000():
    o = Arg()
    o.name = 'ARG'
    assert o.name == 'ARG'


def test_defaults_1_0000():
    o = Arg(name='ARG', lopt='opt')
    o.name = None
    assert o.name == 'OPT'


def test_defaults_2_0000():
    o = Arg(name='ARG', sopt='o')
    o.name = None
    assert o.name == 'O'


def test_defaults_3_0000():
    o = Arg(lopt='lopt', sopt='o')
    o.lopt = None
    o.sopt = None
    assert o.name == ''


def test_exceptions_1_0000():
    o = Arg()
    with pytest.raises(TypeError) as e:
        o.name = 1.
    assert str(e.value) == str(
        'Arg.name: Invalid type: float. '
        'Must be: str, None.'
    )
