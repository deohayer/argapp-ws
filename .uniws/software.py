import toml
from uniws import *


def software() -> 'list[Software]':
    return [Workspace()]


DIR_DIST = f'{DIR_TMP}/dist'
DIR_TEST = f'{DIR_LIB}/test'
DIR_OUT = f'{DIR_TMP}/test'
DOCKERS = {
    '3.6': '18.04',
    '3.7': '19.10',
    '3.8': '20.04',
    '3.9': '21.10',
    '3.10': '22.04',
    '3.11': '23.10',
}


class Workspace(Software):
    def __init__(self) -> 'None':
        super().__init__(name='argapp',
                         help='Work with argapp.')
        self.fetch = Fetch()
        self.build = Build()
        self.install = Install()
        self.test = Test()
        self.release = Release()
        self.clean = Clean()


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
        sh(f'asciidoctor -o {DIR_UWS}/index.html {DIR_UWS}/index.adoc')


class Install(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        sh(f'true'
           f' && rm -rf {DIR_DIST}'
           f' && python3 -m build -wn {DIR_TMP}'
           f' && pip3 install --no-deps --force-reinstall {DIR_TMP}/dist/*'
           f';')


class Test(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        # Build the wheel.
        sh(f'rm -rf {DIR_DIST} && python3 -m build -wn {DIR_TMP}')
        result = True
        results = {x: True for x in DOCKERS}
        for x in DOCKERS:
            sep = '-' * 40
            print(sep)
            print(f'Preparing image for {x}.')
            sh(f'true'
               f' && docker build'
               f'      --build-arg VERSION={DOCKERS[x]}'
               f'      --tag argapp:{x}'
               f'      {DIR_TEST} > /dev/null'
               f';')
            out = f'{DIR_OUT}/{x}'
            flag = f'{out}/failed'
            print(f'Testing {x}.')
            cmd = str(f'true'
                      f' && source /tmp/venv/bin/activate'
                      f' && export PIP_CACHE_DIR={out}/.cache'
                      f' && rm -rf ${{PIP_CACHE_DIR}}'
                      f' && python3 -m pip install {DIR_DIST}/* > /dev/null'
                      f' && for TEST in {DIR_TEST}/*.py; do'
                      f'        export TEST_NAME=\$(basename \${{TEST}});'
                      f'        export TEST_LOG={out}/\${{TEST_NAME}}.log;'
                      f'        export TEST_TXT={out}/\${{TEST_NAME}}.txt;'
                      f'        python3 -m pytest -vv \${{TEST}} > \${{TEST_LOG}};'
                      f'        if [[ \$? == 1 ]]; then'
                      f'            echo FAIL > \${{TEST_TXT}};'
                      f'            echo FAIL > {flag};'
                      f'        else'
                      f'            echo PASS > \${{TEST_TXT}};'
                      f'        fi;'
                      f'        printf \'%-33s : %s\\n\' \${{TEST_NAME}} \$(cat \${{TEST_TXT}});'
                      f'    done'
                      f';')
            sh(f'true'
               f' && rm -rf {out}'
               f' && mkdir -p {out}'
               f' && docker run'
               f'        --rm'
               f'        --user $(id -u):$(id -g)'
               f'        --volume="{DIR_UWS}:{DIR_UWS}"'
               f'        --volume="/etc/group:/etc/group:ro"'
               f'        --volume="/etc/passwd:/etc/passwd:ro"'
               f'        --volume="/etc/shadow:/etc/shadow:ro"'
               f'        argapp:{x}'
               f'        /bin/bash -c "{cmd}"'
               f';')
            results[x] = not os.path.exists(flag)
        print(sep)
        for k, v in results.items():
            result = result and v
            print(f'Result {k:26} : {"PASS" if v else "FAIL"}')
        print(f'Result {"":26} : {"PASS" if result else "FAIL"}')


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


class Clean(App):
    def __call__(
        self,
        args: 'dict[Arg]' = None,
        apps: 'list[App]' = None,
    ) -> 'None':
        super().__call__(args, apps)
        print('Removing Docker images')
        dockers = ' '.join(f'argapp:{x}' for x in DOCKERS)
        sh(f'docker image rm -f {dockers}')
        print(f'Removing {DIR_OUT}')
        sh(f'rm -rf {DIR_OUT}')
        print(f'Removing {DIR_DIST}')
        sh(f'rm -rf {DIR_DIST}')
