import pathlib
from setuptools import setup, find_packages
version = '1.0.0'

setup(
    name = 'currence-rate-from-banks',
    version= version,
    description='Get and save currence rate',
    author='Vlad Onischuk',
    author_email='vlad.onischuk1234@gmail.com',
    url='https://github.com/Vladon2356/21_Currency_rate_lib.git',
    download_url=f'https://github.com/Vladon2356/21_Currency_rate_lib/archive/v{version}.zip',
    packages=find_packages(),
    install_requires = ['requests','matplotlib',]
)
