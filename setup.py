from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def get_requirements():
    req = []
    for line in open('requirements.txt', 'r'):
        req.append(line.split()[0])
    return req


setup(name='SSHKeyDistribut0r',
      version='0.1.0',
      description='A tool which has been written to make SSH key distribution easier for sysop teams.',
      long_description=long_description,
      url='https://github.com/thomai/SSHKeyDistribut0r',
      author='Thomas Maier',
      author_email='info@wurps.de',
      license='CC BY',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent',
                   'Topic :: Communications :: File Sharing',
                   'Topic :: Security',
                   'Topic :: Security :: Cryptography',
                   'Topic :: System :: Networking',
                   'Topic :: System :: Operating System',
                   'Topic :: System :: Shells',
                   'Topic :: System :: Systems Administration',
                   'Topic :: System :: Systems Administration :: Authentication/Directory',
                   'Topic :: System :: System Shells',
                   'Topic :: Terminals',
                   'Topic :: Utilities'],
      keywords='ssh key distribution',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=get_requirements(),
      #extras_require={
      #    'dev': ['check-manifest'],
      #    'test': ['coverage'],
      #},
      #package_data={
      #    'sample': ['package_data.dat'],
      #},
      data_files=[('keys.yml', ['data/keys.yml']),
                  ('servers.yml', ['data/servers.yml'])],
      entry_points={
          'console_scripts': [
              'SSHKeyDistribut0r=SSHKeyDistribut0r:main',
          ],
      },)
