import toml
from uniws import *


def software() -> 'list[Software]':
    return [Workspace()]


class Workspace(Software):
    def __init__(self) -> 'None':
        super().__init__(name='argapp',
                         help='Work with argapp.')
        self.fetch = Fetch()
        self.build = Build()
        self.install = Install()
        self.release = Release()


class Fetch(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        sh(f'true'
           f' && git -C {DIR_UWS} checkout develop'
           f' && git -C {DIR_UWS} submodule update --init'
           f' && git -C {DIR_TMP}/argapp checkout develop'
           f';')


class Build(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        sh(f'asciidoctor -o {DIR_TMP}/argapp/index.html {DIR_TMP}/argapp/index.adoc')


class Install(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        sh(f'true'
           f' && rm -rf {DIR_TMP}/dist'
           f' && python3 -m build -wn {DIR_TMP}'
           f' && pip3 install --no-deps --force-reinstall {DIR_TMP}/dist/*'
           f';')


class Release(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        config = toml.load(f'{DIR_TMP}/pyproject.toml')
        version = config['project']['version']
        root = f'{DIR_TMP}/argapp-ws'
        tmp = f'{root}/tmp'
        repo = f'{tmp}/argapp'
        sh(f'true'
           f' && rm -rf {root}'
           f' && git clone'
           f'      --recurse-submodules'
           f'      --branch main'
           f'      git@github.com:deohayer/argapp-ws.git'
           f'      {root}'
           f' && git -C {root} tag {version}'
           f' && git -C {root} push --tags'
           f' && git -C {repo} tag {version}'
           f' && git -C {repo} push --tags'
           f' && rm -rf {tmp}/dist'
           f' && python3 -m build -wn {tmp}'
           f' && twine upload -r pypi {tmp}/dist/*'
           f';')
