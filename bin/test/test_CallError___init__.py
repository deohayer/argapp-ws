from .core import *


def test_description_0_0000():
    o = CallError()
    assert o.text == ''
    assert o.code == 1


def test_description_0_0001():
    o = CallError('Error', 1)
    assert o.text == 'Error'
    assert o.code == 1


def test_parameters_1_0000():
    o = CallError(text='Error.')
    assert o.text == 'Error.'


def test_parameters_1_0001():
    o = CallError(text=None)
    assert o.text == ''


def test_parameters_1_0002():
    with pytest.raises(TypeError) as e:
        CallError(text=1.)
    assert str(e.value) == str(
        'CallError.text: Invalid type: float. '
        'Must be: str, None.')


def test_parameters_2_0000():
    o = CallError(code=2)
    assert o.code == 2


def test_parameters_2_0001():
    o = CallError(code=None)
    assert o.code == 1


def test_parameters_2_0002():
    with pytest.raises(TypeError) as e:
        CallError(code=1.)
    assert str(e.value) == str(
        'CallError.code: Invalid type: float. '
        'Must be: int, None.')


def test_parameters_2_0003():
    with pytest.raises(ValueError) as e:
        CallError(code=256)
    assert str(e.value) == str(
        'CallError.code: Invalid value: 256. '
        'Must be from 0 to 255.')
