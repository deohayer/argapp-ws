from .core import *


def test_0_0000():
    # Dafault.
    o = CallError()
    assert o.text == ''
    assert o.code == 1


def test_0_0001():
    # All.
    o = CallError('Error', 5)
    assert o.text == 'Error'
    assert o.code == 5


def test_parameters_1_0000():
    # test_0_0000
    assert CallError(text='Error').text == 'Error'


def test_parameters_1_0001():
    # test_defaults_1_0000
    assert CallError(text=None).text == ''


def test_parameters_1_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        CallError(text=1.)
    assert str(e.value) == str(
        'CallError.text: Invalid type: float. '
        'Must be: str, None.'
    )


def test_parameters_2_0000():
    # test_0_0000
    assert CallError(code=2).code == 2


def test_parameters_2_0001():
    # test_defaults_1_0000
    assert CallError(code=None).code == 1


def test_parameters_2_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        CallError(code=1.)
    assert str(e.value) == str(
        'CallError.code: Invalid type: float. '
        'Must be: int, None.'
    )


def test_parameters_2_0003():
    # test_exceptions_2_0000
    with pytest.raises(ValueError) as e:
        CallError(code=256)
    assert str(e.value) == str(
        'CallError.code: Invalid value: 256. '
        'Must be from 0 to 255.'
    )
