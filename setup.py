from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in managelibrary/__init__.py
from managelibrary import __version__ as version

setup(
	name="managelibrary",
	version=version,
	description="to manage all the functions of a library",
	author="sakiya",
	author_email="123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
