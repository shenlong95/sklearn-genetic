import re
from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the version
with open(path.join(here, 'genetic_selection', '__init__.py'), encoding='utf8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sklearn-genetic',
    version=version,
    description='Genetic feature selection module for scikit-learn',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/manuel-calzolari/sklearn-genetic',
    download_url='https://github.com/manuel-calzolari/sklearn-genetic/releases',
    author='Manuel Calzolari',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    python_requires='>=2.7',
    install_requires=['scikit-learn>=0.20.3', 'deap>=1.0.2'],
)
