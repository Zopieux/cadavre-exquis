from setuptools import setup, find_packages

setup(
    name='cadavre-exquis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'irc3',
        'aiocron',
    ],
)
