"""Tools to manage tagging and publishing releases of the Dagster projects.

For detailed usage instructions, please consult the command line help,
available by running `python publish.py --help`.
"""
import contextlib
import os
import re
import subprocess

import click
import packaging.version

from itertools import groupby

PUBLISH_COMMAND = '''rm -rf dist/ && {additional_steps}\\
python setup.py sdist bdist_wheel && \\
twine upload dist/*
'''

DAGIT_ADDITIONAL_STEPS = '''pushd ./dagit/webapp; \\
yarn install && \\
yarn build; \\
popd
'''

MODULE_NAMES = ['dagster', 'dagit', 'dagstermill']


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def path_to_module(module_name):
    relative_path = 'python_modules/{module_name}'.format(
        module_name=module_name)
    return os.path.abspath(relative_path)


@contextlib.contextmanager
def pushd_module(module_name):
    old_cwd = os.getcwd()
    new_cwd = path_to_module(module_name)
    os.chdir(new_cwd)
    try:
        yield new_cwd
    finally:
        os.chdir(old_cwd)


def publish_dagster():
    with pushd_module('dagster') as cwd:
        process = subprocess.Popen(
            PUBLISH_COMMAND.format(additional_steps=''),
            stderr=subprocess.PIPE,
            cwd=cwd,
            shell=True,
            stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            print(line.decode('utf-8'))


def publish_dagit():
    with pushd_module('dagit') as cwd:
        process = subprocess.Popen(
            PUBLISH_COMMAND.format(additional_steps=DAGIT_ADDITIONAL_STEPS),
            stderr=subprocess.PIPE,
            cwd=cwd,
            shell=True,
            stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            print(line.decode('utf-8'))


def publish_dagstermill():
    with pushd_module('dagstermill') as cwd:
        process = subprocess.Popen(
            PUBLISH_COMMAND.format(additional_steps=''),
            stderr=subprocess.PIPE,
            cwd=cwd,
            shell=True,
            stdout=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            print(line.decode('utf-8'))


def publish_all():
    publish_dagster()
    publish_dagit()
    publish_dagstermill()


def get_most_recent_git_tag():
    try:
        git_tag = str(
            subprocess.check_output(
                ['git', 'describe', '--abbrev=0'],
                stderr=subprocess.STDOUT)).strip('\'b\\n')
    except subprocess.CalledProcessError as exc_info:
        raise Exception(str(exc_info.output))
    return git_tag


def get_git_tag():
    try:
        git_tag = str(
            subprocess.check_output(
                ['git', 'describe', '--exact-match', '--abbrev=0'],
                stderr=subprocess.STDOUT)).strip('\'b\\n')
    except subprocess.CalledProcessError as exc_info:
        match = re.search(
            'fatal: no tag exactly matches \'(?P<commit>[a-z0-9]+)\'',
            str(exc_info.output))
        if match:
            raise Exception(
                'Bailing: there is no git tag for the current commit, {commit}'.
                format(commit=match.group('commit')))
        raise Exception(str(exc_info.output))

    return git_tag


def set_git_tag(tag, signed=False):
    try:
        if signed:
            subprocess.check_output(
                ['git', 'tag', '-s', '-m', tag, tag], stderr=subprocess.STDOUT)
        else:
            subprocess.check_output(
                ['git', 'tag', '-a', '-m', tag, tag], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc_info:
        match = re.search('error: gpg failed to sign the data',
                          str(exc_info.output))
        if match:
            raise Exception(
                'Bailing: cannot sign tag. You may find '
                'https://stackoverflow.com/q/39494631/324449 helpful. Original error '
                'output:\n{output}'.format(output=str(exc_info.output)))

        match = re.search('fatal: tag \'(?P<tag>[\.a-z0-9]+)\' already exists',
                          str(exc_info.output))
        if match:
            raise Exception(
                'Bailing: cannot release version tag {tag}: already exists'.
                format(tag=match.group('tag')))
        raise Exception(str(exc_info.output))


def format_module_versions(module_versions):
    return '\n'.join([
        '    {module_name}: {module_version}'.format(
            module_name=module_name, module_version=module_version)
        for module_name, module_version in module_versions.items()
    ])


def get_versions(modules=MODULE_NAMES):
    module_versions = {}
    for module_name in MODULE_NAMES:
        with pushd_module(module_name):
            version = {}
            with open('{module_name}/version.py'.format(
                    module_name=module_name)) as fp:
                exec(fp.read(), version)  # pylint: disable=W0122
            module_versions[module_name] = version['__version__']
    return module_versions


def check_versions_equal():
    module_versions = get_versions()
    assert all_equal(module_versions.values()), \
        'Module versions must be in lockstep to release. Found:\n{versions}'.format(
            versions=format_module_versions(module_versions)
        )
    return module_versions[MODULE_NAMES[0]]


def check_versions():
    version = check_versions_equal()
    git_tag = get_git_tag()

    assert version == git_tag, \
        'Version {version} does not match expected git tag {git_tag}'.format(
            version=version, git_tag=git_tag
        )


def set_new_version(version):
    for module_name in MODULE_NAMES:
        with pushd_module(module_name):
            with open(
                    os.path.abspath('{module_name}/version.py'.format(
                        module_name=module_name)),
                    'w') as fd:
                fd.write(
                    '__version__ = \'{version}\'\n'.format(version=version))


def commit_new_version(version):
    try:
        for module_name in MODULE_NAMES:
            subprocess.check_output(
                [
                    'git', 'add',
                    os.path.join(
                        path_to_module(module_name), module_name, 'version.py')
                ],
                stderr=subprocess.STDOUT)
        subprocess.check_output(
            [
                'git',
                'commit',
                '--no-verify',
                '-m',
                '\'{version}\''.format(version=version),
            ],
            stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc_info:
        raise Exception(exc_info.output)


def check_new_version(version):
    parsed_version = packaging.version.parse(version)
    module_versions = get_versions()
    if not all_equal(module_versions.values()):
        print(
            'Warning! Found repository in a bad state. Existing package versions were not '
            'equal:\n{versions}'.format(
                versions=format_module_versions(module_versions)))
    errors = {}
    for module_name, module_version in module_versions.items():
        if packaging.version.parse(module_version) >= parsed_version:
            errors[module_name] = module_version
    if errors:
        raise Exception(
            'Bailing: Found modules with existing versions greater than or equal to the new version '
            '{version}:\n{versions}'.format(
                version=version,
                versions=format_module_versions(module_versions)))
    return True


def check_git_status():
    changes = subprocess.check_output(['git', 'status', '--porcelain'])
    if changes != b'':
        raise Exception(
            'Bailing: Cannot publish with changes present in git repo:\n{changes}'.
            format(changes=changes))


CLI_HELP = """Tools to help tag and publish releases of the Dagster projects.

By convention, these projects live in a single monorepo, and the submodules are versioned in
lockstep to avoid confusion, i.e., if dagster is at 0.3.0, dagit is also expected to be at
0.3.0.

Versions are tracked in the version.py files present in each submodule and in the git tags
applied to the repository as a whole. These tools help ensure that these versions do not drift.
"""


@click.group(help=CLI_HELP)
def cli():
    pass


@cli.command()
def publish():
    """Publishes (uploads) all submodules to PyPI.
    
    Appropriate credentials must be available to twin, e.g. in a ~/.pypirc file, and users must
    be permissioned as maintainers on the PyPI projects. Publishing will fail if versions (git
    tags and Python versions) are not in lockstep, if the current commit is not tagged, or if
    there are untracked changes.
    """
    print(
        '''WARNING: This will fail (or hang forever) unless you have credentials available to
PyPI, preferably in the form of a ~/.pypirc file as follows:

    [distutils]
    index-servers =
    pypi

    [pypi]
    repository: https://upload.pypi.org/legacy/
    username: <username>
    password: <password>
''')
    print(
        'Checking that module versions are in lockstep and match git tag on most recent commit...'
    )
    check_versions()
    check_git_status()
    print('Publishing packages to PyPI...')
    publish_all()


@cli.command()
@click.argument('version')
def release(version):
    """Tags all submodules for a new release.

    Ensures that git tags, as well as the version.py files in each submodule, agree and that the
    new version is strictly greater than the current version. Will fail if the new version
    is not an increment (following PEP 440). Creates a new git tag and commit.
    """
    check_new_version(version)
    set_new_version(version)
    commit_new_version(version)
    set_git_tag(version)


@cli.command()
def version():
    """Gets the most recent tagged version."""
    print(get_most_recent_git_tag())


cli = click.CommandCollection(sources=[cli], help=CLI_HELP)

if __name__ == '__main__':
    cli()
