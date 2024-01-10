import toml
from uniws import *


def software() -> 'list[Software]':
    '''
    Return a list of Software.

    Returns:
     * list[Software], the list of Software to manipulate.
    '''
    result = [SoftwareArgapp()]
    return result

class SoftwareArgapp(Software):
    def __init__(self) -> 'None':
        super().__init__('argapp', 'Work with argapp.')
        self.root = DIR_UWS
        self.repo = f'{DIR_TMP}/argapp'
        self.toml = f'{DIR_TMP}/pyproject.toml'

    def fetch(self) -> 'None':
        sh(f'true'
           f' && git -C {self.root} checkout develop'
           f' && git -C {self.root} submodule update --init'
           f' && git -C {self.repo} checkout develop'
           f';')

    def install(self) -> 'None':
        sh(f'true'
           f' && rm -rf {DIR_TMP}/dist'
           f' && python3 -m build -wn {DIR_TMP}'
           f' && pip3 install --no-deps --force-reinstall {DIR_TMP}/dist/*'
           f';')

    def release(self) -> 'None':
        config = toml.load(self.toml)
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
