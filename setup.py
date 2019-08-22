
from setuptools import setup, find_packages
from intgen.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='intgen',
    version=VERSION,
    description='Generator of a road intersection specification file',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Ishaan Paranjape',
    author_email='iparanja@ucsc.edu',
    url='https://github.com/AugmentedDesignLab/intgen',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'intgen': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        intgen = intgen.main:main
    """,
)
