from setuptools import setup

VERSION = '0.1'

setup(
    name='sonos-cli',
    version=VERSION,
    author='Bartlomiej Wilczynski',
    author_email='me@bwilczynski.com',
    url='https://github.com/bwilczynski/sonos-cli',
    py_modules=['cli'],
    install_requires=[
        'click',
        'requests',
        'requests_oauthlib',
        'tabulate'
    ],
    entry_points='''
        [console_scripts]
        sonos=sonos.cli:cli
    ''',
)
