"""liba project."""
  
from setuptools import setup, find_packages

setup(
    name='hello',
    version='0.1.0',
    license='none',
    description='hello',

    author='abenben',
    author_email='abenbenben@gmail.com',
    url='https://github.com/abenben/rust-test02',

    packages=find_packages(where=''),
    package_dir={'': '.'},

    install_requires=[],
    extras_require={},

    entry_points={
        'console_scripts': [
            'hello = hello',
        ]
    },
)