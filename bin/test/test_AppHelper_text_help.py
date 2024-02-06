from .core import *

app_prolog = 'This is prolog.'
app_epilog = 'This is epilog.'
app_args_opt = [
    Arg(
        sopt='p',
        lopt='path',
        help='An absolute path.',
        default='/',
        required=True,
    ),
    Arg(
        name='DIR',
        sopt='d',
        lopt='directories',
        count='+',
        help='Directories.',
    ),
]
app_args_pos = [
    Arg(
        name='SRC',
        help='A source path.',
    ),
    Arg(
        name='DST',
        help='A destination path.',
    ),
]
app_apps = [
    App(
        name='app',
    ),
    App(
        name='application',
        help='A subcommand.',
    ),
]


def test_returns_1_1_0000():
    # Nothing is set.
    helper = AppHelper(sopt='', lopt='')
    apps = [App()]
    name = 'main'
    assert helper.text_help(apps, name) == 'main\n'


def test_returns_1_1_0001():
    # Everything is set.
    helper = AppHelper()
    apps = [App(
        prolog=app_prolog,
        epilog=app_epilog,
    )]
    apps[-1].apps.extend(app_apps)
    apps[-1].args.extend(app_args_pos)
    apps[-1].args.extend(app_args_opt)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {-p/--path PATH} SRC DST {...}\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
        '\n'
        'Commands:\n'
        '  app\n'
        '  application    A subcommand.\n'
        '\n'
        'Positional arguments:\n'
        '  SRC    A source path.\n'
        '  DST    A destination path.\n'
        '\n'
        'Optional arguments:\n'
        '  -p/--path PATH                   An absolute path.\n'
        '                                   Default: /\n'
        '  -d/--directories DIR [DIR...]    Directories.\n'
        '  -h/--help                        Show the help text and exit.\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
    )


def test_returns_1_2_0000():
    # Description.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        prolog=app_prolog,
    )]
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
    )


def test_returns_1_2_0001():
    # No description.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        epilog=app_epilog,
    )]
    apps[-1].apps.extend(app_apps)
    apps[-1].args.extend(app_args_pos)
    apps[-1].args.extend(app_args_opt)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {-p/--path PATH} SRC DST {...}\n'
        '\n'
        'Commands:\n'
        '  app\n'
        '  application    A subcommand.\n'
        '\n'
        'Positional arguments:\n'
        '  SRC    A source path.\n'
        '  DST    A destination path.\n'
        '\n'
        'Optional arguments:\n'
        '  -p/--path PATH                   An absolute path.\n'
        '                                   Default: /\n'
        '  -d/--directories DIR [DIR...]    Directories.\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
    )


def test_returns_1_3_0000():
    # Commands.
    helper = AppHelper(sopt='', lopt='')
    apps = [App()]
    apps[-1].apps.extend(app_apps)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {...}\n'
        '\n'
        'Commands:\n'
        '  app\n'
        '  application    A subcommand.\n'
    )


def test_returns_1_3_0001():
    # No commands.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        prolog=app_prolog,
        epilog=app_epilog,
    )]
    apps[-1].args.extend(app_args_pos)
    apps[-1].args.extend(app_args_opt)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {-p/--path PATH} SRC DST\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
        '\n'
        'Positional arguments:\n'
        '  SRC    A source path.\n'
        '  DST    A destination path.\n'
        '\n'
        'Optional arguments:\n'
        '  -p/--path PATH                   An absolute path.\n'
        '                                   Default: /\n'
        '  -d/--directories DIR [DIR...]    Directories.\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
    )


def test_returns_1_4_0000():
    # Positional arguments.
    helper = AppHelper(sopt='', lopt='')
    apps = [App()]
    apps[-1].args.extend(app_args_pos)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main SRC DST\n'
        '\n'
        'Positional arguments:\n'
        '  SRC    A source path.\n'
        '  DST    A destination path.\n'
    )


def test_returns_1_4_0001():
    # No positional arguments.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        prolog=app_prolog,
        epilog=app_epilog,
    )]
    apps[-1].apps.extend(app_apps)
    apps[-1].args.extend(app_args_opt)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {-p/--path PATH} {...}\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
        '\n'
        'Commands:\n'
        '  app\n'
        '  application    A subcommand.\n'
        '\n'
        'Optional arguments:\n'
        '  -p/--path PATH                   An absolute path.\n'
        '                                   Default: /\n'
        '  -d/--directories DIR [DIR...]    Directories.\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
    )


def test_returns_1_5_0000():
    # Optional arguments.
    helper = AppHelper(sopt='', lopt='')
    apps = [App()]
    apps[-1].args.extend(app_args_opt)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {-p/--path PATH}\n'
        '\n'
        'Optional arguments:\n'
        '  -p/--path PATH                   An absolute path.\n'
        '                                   Default: /\n'
        '  -d/--directories DIR [DIR...]    Directories.\n'
    )


def test_returns_1_5_0001():
    # No optional arguments.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        prolog=app_prolog,
        epilog=app_epilog,
    )]
    apps[-1].apps.extend(app_apps)
    apps[-1].args.extend(app_args_pos)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main SRC DST {...}\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
        '\n'
        'Commands:\n'
        '  app\n'
        '  application    A subcommand.\n'
        '\n'
        'Positional arguments:\n'
        '  SRC    A source path.\n'
        '  DST    A destination path.\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
    )


def test_returns_1_6_0000():
    # Epilog.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        epilog=app_epilog,
    )]
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main\n'
        '\n'
        'Notes:\n'
        'This is epilog.\n'
    )


def test_returns_1_6_0001():
    # No epilog.
    helper = AppHelper(sopt='', lopt='')
    apps = [App(
        prolog=app_prolog,
    )]
    apps[-1].apps.extend(app_apps)
    apps[-1].args.extend(app_args_pos)
    apps[-1].args.extend(app_args_opt)
    name = 'main'
    assert helper.text_help(apps, name) == str(
        'main {-p/--path PATH} SRC DST {...}\n'
        '\n'
        'Description:\n'
        'This is prolog.\n'
        '\n'
        'Commands:\n'
        '  app\n'
        '  application    A subcommand.\n'
        '\n'
        'Positional arguments:\n'
        '  SRC    A source path.\n'
        '  DST    A destination path.\n'
        '\n'
        'Optional arguments:\n'
        '  -p/--path PATH                   An absolute path.\n'
        '                                   Default: /\n'
        '  -d/--directories DIR [DIR...]    Directories.\n'
    )
