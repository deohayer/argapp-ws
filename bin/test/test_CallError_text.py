from .core import *


def test_description_0_0000():
    o = CallError()
    o.text = 'Error.'
    assert o.text == 'Error.'


def test_defaults_1_0000():
    o = CallError(text='Error.')
    o.text = None
    assert o.text == ''


def test_exceptions_1_0000():
    o = CallError()
    with pytest.raises(TypeError) as e:
        o.text = 1.
    assert str(e.value) == str(
        'CallError.text: Invalid type: float. '
        'Must be: str, None.')
