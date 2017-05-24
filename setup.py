from setuptools import setup

with open ('README.rst') as f:
    long_description = f.read()

setup(
    name='wslexplorer',
    version='0.1.2',
    description='Simple script that launches Window Explorer from Windows Subsystem for Linux',
    long_description=long_description,
    url='https://github.com/scottfp/wslexplorer',
    author='Scott Pritchard',
    author_email='scottfp@gmail.com',
    license='MIT',
    py_modules=['wslexplorer.win_explorer',
                'wslexplorer.config'],
    install_requires=[
        'Click',
        'ruamel.yaml'
    ],
    entry_points='''
        [console_scripts]
        wslexplorer=wslexplorer.win_explorer:launch
    '''
)
