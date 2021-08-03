from setuptools import setup, find_packages

with open('requirements.txt') as f:
  install_requires = f.read().strip().split('\n')

# get version from __version__ variable in betterpdf/__init__.py
from betterpdf import __version__ as version

setup(
    name='betterpdf',
    version=version,
    description='Better PDF generator',
    author='Senwize B.V.',
    author_email='timvanosch@senwize.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
