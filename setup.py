from setuptools import setup
from pathlib import Path

folder = Path(__file__)
requirements_file = folder.parents[0] / 'requirements.txt'

requires = []
if requirements_file.exists():
    with open(requirements_file) as f:
        requires = f.read().splitlines()

setup(
    name='heic2x',
    version='0.0.1',
    description='A quick program to convert from heic to other image formtas.',
    url='https://github.com/Red-Sage/heic2x.git',
    author='Red Sage',
    author_email='red.sage@outlool.com',
    license='All Rights Reserved',
    install_requires=requires,
    


)