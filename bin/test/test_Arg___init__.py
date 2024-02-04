from .core import *


def test_0_0000():
    # Default.
    o = Arg()
    assert o.name == ''
    assert o.lopt == ''
    assert o.sopt == ''
    assert o.help == ''
    assert o.helper.choices is True
    assert o.helper.default is True
    assert o.type is str
    assert o.count == 1
    assert o.default is None
    assert o.choices == {}
    assert o.restrict is True
    assert o.suppress is False
    assert o.required is True
    assert o.append is False
    assert isinstance(o.completer, CompleterPath)
    assert o.optional is False
    assert o.positional is True
    assert o.flag is False
    assert o.single is True
    assert o.multiple is False


def test_0_0001():
    # All.
    helper = ArgHelper(False, False)
    completer = CompleterNone()
    o = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        help='Help.',
        helper=helper,
        type=int,
        count='+',
        default=[1],
        choices=[1, 2],
        restrict=False,
        suppress=True,
        required=False,
        append=True,
        completer=completer,
    )
    assert o.name == 'ARG'
    assert o.lopt == 'arg'
    assert o.sopt == 'a'
    assert o.help == 'Help.'
    assert o.helper is helper
    assert o.type is int
    assert o.count == '+'
    assert o.default == [1]
    assert o.choices == {'1': '', '2': ''}
    assert o.restrict is False
    assert o.suppress is True
    assert o.required is False
    assert o.append is True
    assert o.completer is completer
    assert o.optional is True
    assert o.positional is False
    assert o.flag is False
    assert o.single is False
    assert o.multiple is True


def test_parameters_1_0000():
    # test_0_0000
    o = Arg(name='ARG')
    assert o.name == 'ARG'


def test_parameters_1_0001():
    # test_defaults_1_0000
    o = Arg(name=None, lopt='opt')
    assert o.name == 'OPT'


def test_parameters_1_0002():
    # test_defaults_2_0000
    o = Arg(name=None, sopt='o')
    assert o.name == 'O'


def test_parameters_1_0003():
    # test_defaults_3_0000
    o = Arg(name=None)
    assert o.name == ''


def test_parameters_1_0004():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(name=1.)
    assert str(e.value) == str(
        'Arg.name: Invalid type: float. '
        'Must be: str, None.'
    )


def test_parameters_2_0000():
    # test_0_0000
    o = Arg(lopt='lopt')
    assert o.lopt == 'lopt'


def test_parameters_2_0001():
    # test_defaults_1_0000
    o = Arg(lopt=None)
    assert o.lopt == ''


def test_parameters_2_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(lopt=1.)
    assert str(e.value) == str(
        'Arg.lopt: Invalid type: float. '
        'Must be: str, None.'
    )


def test_parameters_3_0000():
    # test_0_0000
    o = Arg(sopt='o')
    assert o.sopt == 'o'


def test_parameters_3_0001():
    # test_defaults_1_0000
    o = Arg(sopt=None)
    assert o.sopt == ''


def test_parameters_3_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(sopt=1.)
    assert str(e.value) == str(
        'Arg.sopt: Invalid type: float. '
        'Must be: str, None.'
    )


def test_parameters_3_0003():
    # test_exceptions_2_0000
    with pytest.raises(ValueError) as e:
        Arg(sopt='long')
    assert str(e.value) == str(
        'Arg.sopt: Invalid value: "long". '
        'Must not exceed one character.'
    )


def test_parameters_4_0000():
    # test_0_0000
    o = Arg(help='help')
    assert o.help == 'help'


def test_parameters_4_0001():
    # test_defaults_1_0000
    o = Arg(help=None)
    assert o.help == ''


def test_parameters_4_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(help=1.)
    assert str(e.value) == str(
        'Arg.help: Invalid type: float. '
        'Must be: str, None.'
    )


def test_parameters_5_0000():
    # test_0_0000
    helper = ArgHelper()
    o = Arg(helper=helper)
    assert o.helper is helper


def test_parameters_5_0001():
    # test_defaults_1_0000
    o = Arg(helper=None)
    assert o.helper.choices is True
    assert o.helper.default is True


def test_parameters_5_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(helper=1.)
    assert str(e.value) == str(
        'Arg.helper: Invalid type: float. '
        'Must be: ArgHelper, None.'
    )


def test_parameters_6_0000():
    # test_0_0000
    o = Arg(type=int)
    assert o.type is int


def test_parameters_6_0001():
    # test_defaults_1_0000
    o = Arg(type=int, count=0, sopt='o')
    assert o.type is bool


def test_parameters_6_0002():
    # test_defaults_2_0000
    o = Arg(type=None, default=[5])
    assert o.type is int


def test_parameters_6_0003():
    # test_defaults_3_0000
    o = Arg(type=None, default=False)
    assert o.type is bool


def test_parameters_6_0004():
    # test_defaults_4_0000
    o = Arg(type=None)
    assert o.type is str


def test_parameters_6_0005():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(type=1.)
    assert str(e.value) == str(
        'Arg.type: Invalid type: float. '
        'Must be: type, None.'
    )


def test_parameters_6_0006():
    # test_exceptions_2_0000
    o = Arg(default=6)
    with pytest.raises(ValueError) as e:
        o.type = float
    assert str(e.value) == str(
        'Arg.type: Invalid value: float. '
        'Must match self.default: int.'
    )


def test_parameters_7_0000():
    # test_1_0000
    o = Arg(count=0, sopt='o')
    assert o.count == 0


def test_parameters_7_0001():
    # test_2_0000
    o = Arg(count=1)
    assert o.count == 1


def test_parameters_7_0002():
    # test_3_0000
    o = Arg(count=2)
    assert o.count == 2


def test_parameters_7_0003():
    # test_4_0000
    o = Arg(count='?')
    assert o.count == '?'


def test_parameters_7_0004():
    # test_5_0000
    o = Arg(count='*')
    assert o.count == '*'


def test_parameters_7_0005():
    # test_6_0000
    o = Arg()
    o.count = '+'
    assert o.count == '+'


def test_parameters_7_0006():
    # test_7_0000
    o = Arg()
    o.count = '~'
    assert o.count == '~'


def test_parameters_7_0007():
    # test_defaults_1_0000
    o = Arg(count=None, default=[1])
    assert o.count == '*'


def test_parameters_7_0008():
    # test_defaults_2_0000
    o = Arg(count=None)
    assert o.count == 1


def test_parameters_7_0009():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(count=1.)
    assert str(e.value) == str(
        'Arg.count: Invalid type: float. '
        'Must be: int, str, None.')


def test_parameters_7_0010():
    # test_exceptions_2_0000
    with pytest.raises(ValueError) as e:
        Arg(count=-3)
    assert str(e.value) == str(
        'Arg.count: Invalid value: -3. '
        'Must be positive for positional.')


def test_parameters_7_0011():
    # test_exceptions_3_0000
    with pytest.raises(ValueError) as e:
        Arg(count='$')
    assert str(e.value) == str(
        'Arg.count: Invalid value: "$". '
        'Must be "?", "*", "+" or "~" for positional.')


def test_parameters_7_0012():
    # test_exceptions_4_0000
    with pytest.raises(ValueError) as e:
        Arg(count=0)
    assert str(e.value) == str(
        'Arg.count: Invalid value: 0. '
        'Must be positive for positional.')


def test_parameters_7_0013():
    # test_exceptions_5_0000
    with pytest.raises(ValueError) as e:
        Arg(count='~', sopt='o')
    assert str(e.value) == str(
        'Arg.count: Invalid value: "~". '
        'Must be "?", "*" or "+" for optional.')


def test_parameters_7_0014():
    # test_exceptions_6_0000
    # Cannot be triggered due to the assignment order.
    pass


def test_parameters_7_0015():
    # test_exceptions_7_0000
    # Cannot be triggered due to the assignment order.
    pass


def test_parameters_8_0000():
    # test_0_0000
    o = Arg(default=3)
    assert o.default == 3


def test_parameters_8_0001():
    # test_defaults_1_0000
    o = Arg(default=None, sopt='o', count=0)
    assert o.default is False


def test_parameters_8_0002():
    # test_defaults_2_0000
    o = Arg(default=None, count='*')
    assert o.default == []


def test_parameters_8_0003():
    # test_defaults_3_0000
    o = Arg(default=None)
    assert o.default is None


def test_parameters_8_0004():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(default='abc', count='+')
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: list, None.')


def test_parameters_8_0005():
    # test_exceptions_2_0000
    with pytest.raises(TypeError) as e:
        Arg(default=['a', 'b', 'c'], count=1)
    assert str(e.value) == str(
        'Arg.default: Invalid type: list. '
        'Must be: object, None.')


def test_parameters_8_0006():
    # test_exceptions_3_0000
    with pytest.raises(TypeError) as e:
        Arg(default='1', type=int)
    assert str(e.value) == str(
        'Arg.default: Invalid type: str. '
        'Must be: int, None.')


def test_parameters_8_0007():
    # test_exceptions_4_0000
    with pytest.raises(TypeError) as e:
        Arg(default=[1, '2', 3], type=int)
    assert str(e.value) == str(
        'Arg.default[1]: Invalid type: str. '
        'Must be: int.')


def test_parameters_8_0008():
    # test_exceptions_5_0000
    with pytest.raises(ValueError) as e:
        Arg(default=[1], count=2)
    assert str(e.value) == str(
        'Arg.default: Invalid value: len() is 1. '
        'Must match self.count: 2.')


def test_parameters_8_0009():
    # test_exceptions_6_0000
    with pytest.raises(ValueError) as e:
        Arg(default=[], count='+')
    assert str(e.value) == str(
        'Arg.default: Invalid value: []. '
        'Must have at least one item, self.count is "+".')


def test_parameters_9_0000():
    # test_0_0000
    o = Arg(
        choices={
            '1': '1',
            '2': '2',
        },
    )
    assert o.choices == {
        '1': '1',
        '2': '2',
    }


def test_parameters_9_0001():
    # test_defaults_1_0000
    o = Arg(choices=None)
    assert o.choices == {}


def test_parameters_9_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(choices=1.)
    assert str(e.value) == str(
        'Arg.choices: Invalid type: float. '
        'Must be: Iterable, None.')


def test_parameters_10_0000():
    # test_0_0000
    o = Arg(restrict=False)
    assert o.restrict is False


def test_parameters_10_0001():
    # test_defaults_1_0000
    o = Arg(restrict=None)
    assert o.restrict is True


def test_parameters_10_0002():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(restrict=1.)
    assert str(e.value) == str(
        'Arg.restrict: Invalid type: float. '
        'Must be: bool, None.'
    )


def test_parameters_11_0000():
    # test_0_0000
    o = Arg(suppress=True, sopt='o')
    assert o.suppress is True


def test_parameters_11_0001():
    # test_defaults_1_0000
    o = Arg(suppress=None)
    assert o.suppress is False


def test_parameters_11_0002():
    # test_defaults_2_0000
    o = Arg(suppress=None, sopt='o')
    assert o.suppress is False


def test_parameters_11_0003():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(suppress=1., sopt='o')
    assert str(e.value) == str(
        'Arg.suppress: Invalid type: float. '
        'Must be: bool, None.')


def test_parameters_12_0000():
    # test_0_0000
    o = Arg(required=False, sopt='o')
    assert o.required is False


def test_parameters_12_0001():
    # test_defaults_1_0000
    o = Arg(required=False)
    assert o.required is True


def test_parameters_12_0002():
    # test_defaults_2_0000
    o = Arg(required=None, sopt='o')
    assert o.required is False


def test_parameters_12_0003():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(required=1., sopt='o')
    assert str(e.value) == str(
        'Arg.required: Invalid type: float. '
        'Must be: bool, None.')


def test_parameters_13_0000():
    # test_0_0000
    o = Arg(sopt='o', append=True)
    assert o.append is True


def test_parameters_13_0001():
    # test_defaults_1_0000
    o = Arg(append=True)
    assert o.append is False


def test_parameters_13_0002():
    # test_defaults_2_0000
    o = Arg(sopt='o', append=None)
    assert o.append is False


def test_parameters_13_0003():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(append=1.)
    assert str(e.value) == str(
        'Arg.append: Invalid type: float. '
        'Must be: bool, None.'
    )


def test_parameters_14_0000():
    # test_0_0000
    completer = CompleterList(['a', 'b', 'c'])
    o = Arg(completer=completer)
    assert o.completer is completer


def test_parameters_14_0001():
    # test_defaults_1_0000
    o = Arg(completer=None, choices=[1, 2, 3])
    assert isinstance(o.completer, CompleterList)


def test_parameters_14_0002():
    # test_defaults_2_0000
    o = Arg(completer=None, type=str)
    assert isinstance(o.completer, CompleterPath)


def test_parameters_14_0003():
    # test_defaults_3_0000
    o = Arg(completer=None, type=int)
    assert isinstance(o.completer, CompleterNone)


def test_parameters_14_0004():
    # test_exceptions_1_0000
    with pytest.raises(TypeError) as e:
        Arg(completer=1.)
    assert str(e.value) == str(
        'Arg.completer: Invalid type: float. '
        'Must be: Completer, None.')
