from invoke import run
from twine.commands import upload as twine_upload
import configparser
config = configparser.ConfigParser()

def upload_to_pypi(dists='sdist bdist_wheel', config_file='~/.pypirc', skip_existing=False):
    """
    Creates the wheel and uploads to pypi with twine.

    :param dists: The dists string passed to setup.py. Default: 'bdist_wheel'
    """
    run('python setup.py {}'.format(dists))
    pypirc_cfg = config.read(config_file)

    twine_upload.upload(
        dists=['dist/*'],
        repository=pypirc_cfg['pipy']['repository'],
        sign=False,
        identity=None,
        username=pypirc_cfg['pipy']['username'],
        password=pypirc_cfg['pipy']['password'],
        comment=None,
        sign_with='gpg',
        config_file=config_file,
        skip_existing=skip_existing,
        cert=None,
        client_cert=None,
        repository_url=None
    )
    run('rm -rf build dist')
