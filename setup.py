from setuptools import setup

setup(
    name='sonos-cli',
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'click',
        'requests',
        'requests_oauthlib',
        'tabulate'
    ],
    entry_points='''
        [console_scripts]
        sonos-cli=cli:cli
    ''',
)