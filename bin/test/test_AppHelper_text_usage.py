from .core import *


def test_returns_1_0000():
    # A single app, no name.
    helper = AppHelper()
    apps = [App()]
    name = 'name'
    assert helper.text_usage(apps, name) == 'name'


def test_returns_1_0001():
    # A single app, no arguments.
    helper = AppHelper()
    apps = [App(name='app')]
    name = 'name'
    assert helper.text_usage(apps, name) == 'app'


def test_returns_1_0002():
    # A single app, one positional.
    helper = AppHelper()
    apps = [App()]
    apps[0].args.append(Arg(name='ARG'))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name ARG'


def test_returns_1_0003():
    # A single app, one non-required optional.
    helper = AppHelper()
    apps = [App()]
    apps[0].args.append(Arg(lopt='arg'))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name'


def test_returns_1_0004():
    # A single app, one required optional.
    helper = AppHelper()
    apps = [App()]
    apps[0].args.append(Arg(lopt='arg', required=True))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name {--arg ARG}'


def test_returns_1_0005():
    # A single app, subapps.
    helper = AppHelper()
    apps = [App()]
    apps[0].apps.append(App('app'))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name (...)'


def test_returns_1_0006():
    # A single app, multiple arguments and subapps.
    assert AppHelper().section_apps('Title', []) == ''
    helper = AppHelper()
    apps = [App()]
    apps[0].args.append(Arg(name='ARG'))
    apps[0].args.append(Arg(lopt='arg', required=True))
    apps[0].apps.append(App('app'))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name {--arg ARG} ARG (...)'


def test_returns_1_0007():
    # Multiple apps, no name.
    helper = AppHelper()
    apps = [App(), App(name='app')]
    name = 'name'
    assert helper.text_usage(apps, name) == 'name app'


def test_returns_1_0008():
    # Multiple apps, no arguments.
    helper = AppHelper()
    apps = [App(name='main'), App(name='app')]
    name = 'name'
    assert helper.text_usage(apps, name) == 'main app'


def test_returns_1_0009():
    # Multiple apps, the last with arguments and subapps.
    helper = AppHelper()
    apps = [App(), App(name='app')]
    apps[1].args.append(Arg(name='ARG'))
    apps[1].args.append(Arg(lopt='arg', required=True))
    apps[1].apps.append(App('sub'))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name app {--arg ARG} ARG (...)'


def test_returns_1_0010():
    # Multiple apps, all with arguments and subapps.
    helper = AppHelper()
    apps = [App(), App(name='app')]
    apps[0].args.append(Arg(name='ARG1'))
    apps[0].args.append(Arg(lopt='arg1', required=True))
    apps[0].apps.append(App('sub1'))
    apps[1].args.append(Arg(name='ARG'))
    apps[1].args.append(Arg(lopt='arg', required=True))
    apps[1].apps.append(App('sub'))
    name = 'name'
    assert helper.text_usage(apps, name) == 'name app {--arg ARG} ARG (...)'
