from setuptools import setup

setup(
    name='python_ignore',
    version='0.0.1',
    description='run addPythonIgnore on command line to create your python gitignore file',
    packages=['python_ignore'],
    entry_points = {
        'console_scripts': ['addPythonIgnore=python_ignore:main']
    }
)