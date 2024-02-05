import sys
from argapp import App, AppHelper, Arg
from .core import *


def check_output(
    capsys,
    app: 'App',
    argv: 'list[str]' = None,
    stdout: 'str' = '',
    stderr: 'str' = '',
    code: 'int | None' = None,
    error: 'Exception' = SystemExit()
) -> 'None':
    if code is None:
        code = 1 if stderr else 0
    with pytest.raises(type(error)) as e:
        capsys.readouterr()
        if argv is not None:
            main(app, argv)
        else:
            main(app)
    if type(error) is not SystemExit:
        assert str(error) == str(e.value)
    else:
        assert e.value.code == code
    std = capsys.readouterr()
    assert std.out == stdout
    assert std.err == stderr


def check_parse(
    arg: 'Arg',
    v: 'object',
    argv: 'list[str]',
) -> 'None':
    class TestApp(App):
        def __call__(
            self,
            args: 'dict[Arg]',
            apps: 'list[App]',
        ) -> 'None':
            if not arg.suppress:
                assert args[arg] == v
            else:
                if f'-{arg.sopt}' not in argv:
                    assert arg not in args

    app = TestApp('app')
    app.args.append(arg)
    with pytest.raises(SystemExit) as e:
        main(app, argv)
    assert e.value.code == 0


def test_1_0000(capsys):
    # Construction: app.name - set.
    app = App(name='app')
    stdout = str(
        'app\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['path/to/app', '-h'],
        stdout=stdout,
    )


def test_1_0001(capsys):
    # Construction: app.name - not set.
    app = App()
    stdout = str(
        'app\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['path/to/app', '-h'],
        stdout=stdout,
    )


def test_2_0000():
    # Parsing: long and short options.
    arg = Arg(
        lopt='arg',
        sopt='a',
    )
    check_parse(arg, 'v', ['app', '-a', 'v'])
    check_parse(arg, 'v', ['app', '--arg', 'v'])


def test_2_0001():
    # Parsing: Arg - optional, 0, no default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=0,
        default=None,
        append=None,
    )
    check_parse(arg, False, ['app'])
    check_parse(arg, True, ['app', '-a'])


def test_2_0002():
    # Parsing: Arg - optional, 0, default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=0,
        default=True,
        append=None,
    )
    check_parse(arg, True, ['app'])
    check_parse(arg, False, ['app', '-a'])


def test_2_0003():
    # Parsing: Arg - optional, 0, no default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=0,
        default=None,
        append=True,
    )
    check_parse(arg, 0, ['app'])
    check_parse(arg, 1, ['app', '-a'])
    check_parse(arg, 2, ['app', '-a', '-a'])


def test_2_0004():
    # Parsing: Arg - positional, 1, no default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count=1,
        default=None,
        append=None,
    )
    check_parse(arg, 'v', ['app', 'v'])


def test_2_0005():
    # Parsing: Arg - optional, 1, no default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=1,
        default=None,
        append=None,
    )
    check_parse(arg, None, ['app'])
    check_parse(arg, 'v', ['app', '-a', 'v'])


def test_2_0006():
    # Parsing: Arg - optional, 1, default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=1,
        default='V',
        append=None,
    )
    check_parse(arg, 'V', ['app'])
    check_parse(arg, 'v', ['app', '-a', 'v'])


def test_2_0007():
    # Parsing: Arg - optional, 1, no default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=1,
        default=None,
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, ['v'], ['app', '-a', 'v'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', '-a', 'v2'])


def test_2_0008():
    # Parsing: Arg - optional, 1, default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=1,
        default='V',
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, ['v'], ['app', '-a', 'v'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', '-a', 'v2'])


def test_2_0009():
    # Parsing: Arg - positional, '?', no default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='?',
        default=None,
        append=None,
    )
    check_parse(arg, None, ['app'])
    check_parse(arg, 'v', ['app', 'v'])


def test_2_0010():
    # Parsing: Arg - positional, '?', default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='?',
        default='V',
        append=None,
    )
    check_parse(arg, 'V', ['app'])
    check_parse(arg, 'v', ['app', 'v'])


def test_2_0011():
    # Parsing: Arg - optional, '?', no default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='?',
        default=None,
        append=None,
    )
    check_parse(arg, None, ['app'])
    check_parse(arg, None, ['app', '-a'])
    check_parse(arg, 'v', ['app', '-a', 'v'])


def test_2_0012():
    # Parsing: Arg - optional, '?', default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='?',
        default='V',
        append=None,
    )
    check_parse(arg, 'V', ['app'])
    check_parse(arg, 'V', ['app', '-a'])
    check_parse(arg, 'v', ['app', '-a', 'v'])


def test_2_0013():
    # Parsing: Arg - optional, '?', no default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='?',
        default=None,
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [None], ['app', '-a'])
    check_parse(arg, [None, 'v'], ['app', '-a', '-a', 'v'])


def test_2_0014():
    # Parsing: Arg - optional, '?', default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='?',
        default='V',
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, ['V'], ['app', '-a'])
    check_parse(arg, ['V', 'v'], ['app', '-a', '-a', 'v'])


def test_2_0015():
    # Parsing: Arg - positional, 2, no default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count=2,
        default=None,
        append=None,
    )
    check_parse(arg, ['v1', 'v2'], ['app', 'v1', 'v2'])


def test_2_0016():
    # Parsing: Arg - optional, 2, no default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=2,
        default=None,
        append=None,
    )
    check_parse(arg, None, ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', 'v2'])


def test_2_0017():
    # Parsing: Arg - optional, 2, default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=2,
        default=['V1', 'V2'],
        append=None,
    )
    check_parse(arg, ['V1', 'V2'], ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', 'v2'])


def test_2_0018():
    # Parsing: Arg - optional, 2, no default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=2,
        default=None,
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [['v1', 'v2']], ['app', '-a', 'v1', 'v2'])
    check_parse(
        arg,
        [['v1', 'v2'], ['v3', 'v4']],
        ['app', '-a', 'v1', 'v2', '-a', 'v3', 'v4'],
    )


def test_2_0019():
    # Parsing: Arg - optional, 2, default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count=2,
        default=['V1', 'V2'],
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [['v1', 'v2']], ['app', '-a', 'v1', 'v2'])
    check_parse(
        arg,
        [['v1', 'v2'], ['v3', 'v4']],
        ['app', '-a', 'v1', 'v2', '-a', 'v3', 'v4'],
    )


def test_2_0020():
    # Parsing: Arg - positional, '*', no default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='*',
        default=None,
        append=None,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', 'v1', 'v2'])


def test_2_0021():
    # Parsing: Arg - positional, '*', default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='*',
        default=['V1', 'V2'],
        append=None,
    )
    check_parse(arg, ['V1', 'V2'], ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', 'v1', 'v2'])


def test_2_0022():
    # Parsing: Arg - optional, '*', no default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='*',
        default=None,
        append=None,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [], ['app', '-a'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', 'v2'])


def test_2_0023():
    # Parsing: Arg - optional, '*', default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='*',
        default=['V1', 'V2'],
        append=None,
    )
    check_parse(arg, ['V1', 'V2'], ['app'])
    check_parse(arg, ['V1', 'V2'], ['app', '-a'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', 'v2'])


def test_2_0024():
    # Parsing: Arg - optional, '*', no default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='*',
        default=None,
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [[]], ['app', '-a'])
    check_parse(arg, [[], ['v1', 'v2']], ['app', '-a', '-a', 'v1', 'v2'])


def test_2_0025():
    # Parsing: Arg - optional, '*', default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='*',
        default=['V1', 'V2'],
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [['V1', 'V2']], ['app', '-a'])
    check_parse(
        arg,
        [['V1', 'V2'], ['v3', 'v4']],
        ['app', '-a', '-a', 'v3', 'v4'],
    )


def test_2_0026():
    # Parsing: Arg - positional, '+', no default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='+',
        default=None,
        append=None,
    )
    check_parse(arg, ['v1', 'v2'], ['app', 'v1', 'v2'])


def test_2_0027():
    # Parsing: Arg - optional, '+', no default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='+',
        default=None,
        append=None,
    )
    check_parse(arg, None, ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', 'v2'])


def test_2_0028():
    # Parsing: Arg - optional, '+', default, no append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='+',
        default=['V1', 'V2'],
        append=None,
    )
    check_parse(arg, ['V1', 'V2'], ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', '-a', 'v1', 'v2'])


def test_2_0029():
    # Parsing: Arg - optional, '+', no default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='+',
        default=None,
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [['v1', 'v2']], ['app', '-a', 'v1', 'v2'])
    check_parse(
        arg,
        [['v1', 'v2'], ['v3', 'v4']],
        ['app', '-a', 'v1', 'v2', '-a', 'v3', 'v4'],
    )


def test_2_0030():
    # Parsing: Arg - optional, '+', default, append.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='+',
        default=['V1', 'V2'],
        append=True,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [['v1', 'v2']], ['app', '-a', 'v1', 'v2'])
    check_parse(
        arg,
        [['v1', 'v2'], ['v3', 'v4']],
        ['app', '-a', 'v1', 'v2', '-a', 'v3', 'v4'],
    )


def test_2_0031():
    # Parsing: Arg - positional, '~', no default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='~',
        default=None,
        append=None,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', 'v1', 'v2'])
    check_parse(arg, ['v1', '-a', 'v2'], ['app', 'v1', '-a', 'v2'])


def test_2_0032():
    # Parsing: Arg - positional, '~', default, no append.
    arg = Arg(
        name='ARG',
        lopt=None,
        sopt=None,
        count='~',
        default=['V1', 'V2'],
        append=None,
    )
    check_parse(arg, ['V1', 'V2'], ['app'])
    check_parse(arg, ['v1', 'v2'], ['app', 'v1', 'v2'])
    check_parse(arg, ['v1', '-a', 'v2'], ['app', 'v1', '-a', 'v2'])


def test_2_0033():
    # Parsing: Arg.choices - valid, restrict.
    arg = Arg(
        name='ARG',
        choices=['v1', 'v2'],
        restrict=True,
    )
    check_parse(arg, 'v1', ['app', 'v1'])
    check_parse(arg, 'v2', ['app', 'v2'])


def test_2_0034():
    # Parsing: Arg.choices - invalid, no restrict.
    arg = Arg(
        name='ARG',
        choices=['v1', 'v2'],
        restrict=False,
    )
    check_parse(arg, 'v1', ['app', 'v1'])
    check_parse(arg, 'v2', ['app', 'v2'])
    check_parse(arg, 'v3', ['app', 'v3'])


def test_2_0035():
    # Parsing: Arg.suppress.
    arg = Arg(
        name='ARG',
        lopt='arg',
        sopt='a',
        count='?',
        suppress=True,
    )
    check_parse(arg, arg, ['app'])
    check_parse(arg, None, ['app', '-a'])
    check_parse(arg, 'v', ['app', '-a', 'v'])


def test_2_0036():
    # Parsing: Arg.type.
    arg = Arg(
        name='ARG',
        count='*',
        type=int,
    )
    check_parse(arg, [], ['app'])
    check_parse(arg, [1], ['app', '1'])
    check_parse(arg, [1, 2], ['app', '1', '2'])


def test_3_0000(capsys):
    # Execution: Help - regular.
    app = App()
    stdout = str(
        'app\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-h'],
        stdout=stdout,
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '--help'],
        stdout=stdout,
    )


def test_3_0001(capsys):
    # Execution: Help - custom.
    app = App(helper=AppHelper(lopt='docs', sopt='d'))
    stdout = str(
        'app\n'
        '\n'
        'Optional arguments:\n'
        '  -d/--docs    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-d'],
        stdout=stdout,
    )


def test_3_0002():
    # Execution: Help - disable.
    class TestApp(App):
        def __init__(self) -> 'None':
            # Disable the help via AppHelper.
            super().__init__(helper=AppHelper(lopt=None, sopt=None))
            # Override the help argument.
            self.arg = Arg(
                lopt='help',
                sopt='h',
                count=0,
            )
            self.args.append(self.arg)

        def __call__(
            self,
            args: 'dict[Arg]',
            apps: 'list[App]',
        ) -> 'None':
            assert args[self.arg] is True

    # Check sopt.
    with pytest.raises(SystemExit) as e:
        main(TestApp(), ['app', '-h'])
    assert e.value.code == 0
    # Check lopt.
    with pytest.raises(SystemExit) as e:
        main(TestApp(), ['app', '--help'])
    assert e.value.code == 0


def test_3_0003(capsys):
    # Execution: Help - first command.
    app = App(name='app0')
    app.apps.append(App(name='app1'))
    app.apps[0].apps.append(App(name='app2'))
    stdout = str(
        'app0 (...)\n'
        '\n'
        'Commands:\n'
        '  app1\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app0', '-h'],
        stdout=stdout,
    )


def test_3_0004(capsys):
    # Execution: Help - middle command.
    app = App(name='app0')
    app.apps.append(App(name='app1'))
    app.apps[0].apps.append(App(name='app2'))
    stdout = str(
        'app0 app1 (...)\n'
        '\n'
        'Commands:\n'
        '  app2\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app0', 'app1', '-h'],
        stdout=stdout,
    )


def test_3_0005(capsys):
    # Execution: Help - last command.
    app = App(name='app0')
    app.apps.append(App(name='app1'))
    app.apps[0].apps.append(App(name='app2'))
    stdout = str(
        'app0 app1 app2\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app0', 'app1', 'app2', '-h'],
        stdout=stdout,
    )


def test_3_0006(capsys):
    # Execution: Help - prolog and epilog.
    app = App(
        prolog='This is prolog.',
        epilog='This is epilog.',
    )
    stdout = str(
        'app\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-h'],
        stdout=stdout,
    )


def test_3_0007(capsys):
    # Execution: Help - all Arg.count.
    app = App()
    app.args.append(Arg(sopt='z', lopt='zero', count=0))
    app.args.append(Arg(sopt='u', lopt='unit', count=1))
    app.args.append(Arg(sopt='d', lopt='dual', count=2))
    app.args.append(Arg(sopt='m', lopt='mark', count='?'))
    app.args.append(Arg(sopt='s', lopt='star', count='*'))
    app.args.append(Arg(sopt='p', lopt='plus', count='+'))
    app.args.append(Arg(name='UNIT', count=1))
    app.args.append(Arg(name='DUAL', count=2))
    app.args.append(Arg(name='MARK', count='?'))
    app.args.append(Arg(name='STAR', count='*'))
    app.args.append(Arg(name='PLUS', count='+'))
    app.args.append(Arg(name='WAVE', count='~'))
    stdout = str(
        'app UNIT DUAL DUAL [MARK] [STAR...] PLUS [PLUS...] [WAVE]...\n'
        '\n'
        'Positional arguments:\n'
        '  UNIT\n'
        '  DUAL DUAL\n'
        '  [MARK]\n'
        '  [STAR...]\n'
        '  PLUS [PLUS...]\n'
        '  [WAVE]...\n'
        '\n'
        'Optional arguments:\n'
        '  -z/--zero\n'
        '  -u/--unit UNIT\n'
        '  -d/--dual DUAL DUAL\n'
        '  -m/--mark [MARK]\n'
        '  -s/--star [STAR...]\n'
        '  -p/--plus PLUS [PLUS...]\n'
        '  -h/--help                   Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-h'],
        stdout=stdout,
    )


def test_3_0008(capsys):
    # Execution: Help - Arg.required.
    app = App()
    app.args.append(Arg(sopt='u', lopt='unit', required=True))
    stdout = str(
        'app {-u/--unit UNIT}\n'
        '\n'
        'Optional arguments:\n'
        '  -u/--unit UNIT\n'
        '  -h/--help         Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-h'],
        stdout=stdout,
    )


def test_3_0009(capsys):
    # Execution: Help - Arg.choices and Arg.default.
    app = App()
    app.args.append(Arg(
        name='UNIT',
        count='?',
        default='v',
        choices=['v', 'w'],
    ))
    stdout = str(
        'app [UNIT]\n'
        '\n'
        'Positional arguments:\n'
        '  [UNIT]    Default: v\n'
        '            Allowed values:\n'
        '             * v\n'
        '             * w\n'
        '\n'
        'Optional arguments:\n'
        '  -h/--help    Show the help text and exit.\n'
        '\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-h'],
        stdout=stdout,
    )


def test_3_0010(capsys):
    # Execution: App - single.
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            print(self.name.capitalize())

    app = AppTest()
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stdout='App\n',
    )


def test_3_0011(capsys):
    # Execution: App - multiple.
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            print(self.name.capitalize())

    app = AppTest()
    app.apps.append(AppTest(name='sub'))
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', 'sub'],
        stdout='App\nSub\n',
    )


def test_parameters_1_0000(capsys):
    # Execution: app - command.
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            print(self.name.capitalize())

    check_output(
        capsys=capsys,
        app=AppTest(),
        argv=['app'],
        stdout='App\n',
    )


def test_parameters_1_0001(capsys):
    # Execution: app - subcommand.
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            print(self.name.capitalize())

    app = AppTest()
    sub = AppTest()
    app.apps.append(sub)
    check_output(
        capsys=capsys,
        app=sub,
        argv=['sub'],
        stdout='Sub\n',
    )


def test_parameters_2_0000(capsys):
    # Execution: argv - default.
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            print(self.name.capitalize())

    app = AppTest()
    argv = [x for x in sys.argv]
    sys.argv = ['app']
    check_output(
        capsys=capsys,
        app=app,
        stdout='App\n',
    )
    sys.argv = argv


def test_parameters_2_0001(capsys):
    # Execution: argv - custom.
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            print(self.name.capitalize())

    app = AppTest()
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stdout='App\n',
    )


def test_exceptions_1_1_0000(capsys):
    # Construction: Subcommand name - empty.
    app = App()
    app.apps.append(App())
    error = ValueError(
        'main: Invalid value: app. '
        'apps[0].name is empty.'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_2_0000(capsys):
    # Construction: Subcommand name - clash.
    app = App()
    app.apps.append(App('sub'))
    app.apps.append(App('sub'))
    error = ValueError(
        'main: Invalid value: app. '
        'apps[0] and apps[1] have the same name: "sub".'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_3_0000(capsys):
    # Construction: Positional argument name - empty.
    app = App()
    app.args.append(Arg())
    error = ValueError(
        'main: Invalid value: app. '
        'args[0].name is empty.'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_4_0000(capsys):
    # Construction: Positional argument clash.
    app = App()
    app.args.append(Arg('arg'))
    app.args.append(Arg('arg'))
    error = ValueError(
        'main: Invalid value: app. '
        'args[0] and args[1] have the same name: "arg".'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_5_0000(capsys):
    # Construction: Optional argument clash - lopt.
    app = App()
    app.args.append(Arg(lopt='arg'))
    app.args.append(Arg(lopt='arg'))
    error = ValueError(
        'main: Invalid value: app. '
        'args[0] and args[1] have the same lopt: "arg".'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_5_0001(capsys):
    # Construction: Optional argument clash - sopt.
    app = App()
    app.args.append(Arg(sopt='a'))
    app.args.append(Arg(sopt='a'))
    error = ValueError(
        'main: Invalid value: app. '
        'args[0] and args[1] have the same sopt: "a".'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_5_0002(capsys):
    # Construction: Optional argument help clash - lopt.
    app = App()
    app.args.append(Arg(lopt='help'))
    error = ValueError(
        'main: Invalid value: app. '
        'args[0] and help have the same lopt: "help".'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_1_5_0003(capsys):
    # Construction: Optional argument help clash - sopt.
    app = App()
    app.args.append(Arg(sopt='h'))
    error = ValueError(
        'main: Invalid value: app. '
        'args[0] and help have the same sopt: "h".'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        error=error,
    )


def test_exceptions_2_1_0000(capsys):
    # Parsing: Custom - not in choices.
    app = App()
    app.args.append(Arg(name='ARG', choices=[1, 2, 3]))
    stderr = str(
        'app ARG\n'
        '\n'
        'Invalid value of argument ARG: 4. Must be one of:\n'
        ' * 1\n'
        ' * 2\n'
        ' * 3\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '4'],
        stderr=stderr,
    )


def test_exceptions_2_2_0000(capsys):
    # Parsing: Subcommand - missing.
    app = App()
    app.apps.append(App('sub0'))
    app.apps.append(App('sub1'))
    app.apps.append(App('sub2'))
    stderr = str(
        'app (...)\n'
        '\n'
        'Missing subcommand. Choose from:\n'
        ' * sub0\n'
        ' * sub1\n'
        ' * sub2\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stderr=stderr,
    )


def test_exceptions_2_3_0000(capsys):
    # Parsing: Subcommand - unknown.
    app = App()
    app.apps.append(App('sub0'))
    app.apps.append(App('sub1'))
    app.apps.append(App('sub2'))
    stderr = str(
        'app (...)\n'
        '\n'
        'Invalid subcommand. Choose from:\n'
        ' * sub0\n'
        ' * sub1\n'
        ' * sub2\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', 'sub3'],
        stderr=stderr,
    )


def test_exceptions_2_4_0000(capsys):
    # Parsing: Arguments - missing positional.
    app = App()
    app.args.append(Arg(name='ARG'))
    stderr = str(
        'app ARG\n'
        '\n'
        'Missing arguments: ARG.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stderr=stderr,
    )


def test_exceptions_2_4_0001(capsys):
    # Parsing: Arguments - missing optional.
    app = App()
    app.args.append(Arg(sopt='o', lopt='opt', required=True))
    stderr = str(
        'app {-o/--opt OPT}\n'
        '\n'
        'Missing arguments: -o/--opt.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stderr=stderr,
    )


def test_exceptions_2_4_0002(capsys):
    # Parsing: Arguments - missing positionals.
    app = App()
    app.args.append(Arg(name='ARG0'))
    app.args.append(Arg(name='ARG1'))
    stderr = str(
        'app ARG0 ARG1\n'
        '\n'
        'Missing arguments: ARG0, ARG1.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stderr=stderr,
    )


def test_exceptions_2_4_0003(capsys):
    # Parsing: Arguments - missing optionals.
    app = App()
    app.args.append(Arg(sopt='o', lopt='opt', required=True))
    app.args.append(Arg(sopt='a', required=True))
    app.args.append(Arg(lopt='arg', required=True))
    stderr = str(
        'app {-o/--opt OPT} {-a A} {--arg ARG}\n'
        '\n'
        'Missing arguments: -o/--opt, -a, --arg.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app'],
        stderr=stderr,
    )


def test_exceptions_2_4_0004(capsys):
    # Parsing: Arguments - missing in-between.
    app = App()
    app.apps.append(App(name='sub'))
    app.args.append(Arg(sopt='o', lopt='opt', required=True))
    stderr = str(
        'app {-o/--opt OPT} (...)\n'
        '\n'
        'Missing arguments: -o/--opt.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', 'sub'],
        stderr=stderr,
    )


def test_exceptions_2_5_0000(capsys):
    # Parsing: Arguments - unknown positional.
    app = App()
    app.args.append(Arg('ARG'))
    stderr = str(
        'app ARG\n'
        '\n'
        'Unknown arguments: sub.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', 'arg', 'sub'],
        stderr=stderr,
    )


def test_exceptions_2_5_0001(capsys):
    # Parsing: Arguments - unknown positionals.
    app = App()
    stderr = str(
        'app\n'
        '\n'
        'Unknown arguments: arg, sub.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', 'arg', 'sub'],
        stderr=stderr,
    )


def test_exceptions_2_5_0002(capsys):
    # Parsing: Arguments - unknown optional.
    app = App()
    app.args.append(Arg('ARG'))
    stderr = str(
        'app ARG\n'
        '\n'
        'Unknown arguments: -o.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-o', 'arg'],
        stderr=stderr,
    )


def test_exceptions_2_5_0003(capsys):
    # Parsing: Arguments - unknown optionals.
    app = App()
    stderr = str(
        'app\n'
        '\n'
        'Unknown arguments: -o, --opt.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-o', '--opt'],
        stderr=stderr,
    )


def test_exceptions_2_6_0000(capsys):
    # Parsing: Arguments - less values (1).
    app = App()
    app.args.append(Arg(sopt='o', lopt='opt', count=1))
    stderr = str(
        'app\n'
        '\n'
        '-o/--opt: expected one value.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-o'],
        stderr=stderr,
    )


def test_exceptions_2_6_0001(capsys):
    # Parsing: Arguments - less values (2).
    app = App()
    app.args.append(Arg(sopt='o', lopt='opt', count=2))
    stderr = str(
        'app\n'
        '\n'
        '-o/--opt: expected 2 values.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-o'],
        stderr=stderr,
    )


def test_exceptions_2_6_0002(capsys):
    # Parsing: Arguments - less values ('+').
    app = App()
    app.args.append(Arg(sopt='o', lopt='opt', count='+'))
    stderr = str(
        'app\n'
        '\n'
        '-o/--opt: expected at least one value.\n'
    )
    check_output(
        capsys=capsys,
        app=app,
        argv=['app', '-o'],
        stderr=stderr,
    )


def test_exceptions_3_1_0000(capsys):
    # Execution: CallError in App.__call__().
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            raise CallError('Error.', 42)

    check_output(
        capsys=capsys,
        app=AppTest(),
        argv=['app'],
        stderr='Error.\n',
        code=42,
    )


def test_exceptions_3_2_0000(capsys):
    # Execution: RuntimeError in App.__call__().
    class AppTest(App):
        def __call__(self, args: 'dict[Arg]', apps: 'list[App]') -> 'None':
            raise RuntimeError('Error.')

    check_output(
        capsys=capsys,
        app=AppTest(),
        argv=['app'],
        error=RuntimeError('Error.'),
    )


def test_exceptions_3_3_0000(capsys):
    # Execution: No errors.
    check_output(
        capsys=capsys,
        app=App(),
        argv=['app'],
    )
