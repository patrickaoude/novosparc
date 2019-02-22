from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

try:
    from novosparc import __author__, __email__
except ImportError:  # Deps not yet installed
    __author__ = __email__ = ''

with open('requirements.txt', 'r') as f:
    required_packages = f.read().splitlines()

setup(
    name="novosparc",
    version="0.3.2",
    author=__author__,
    author_email=__email__,
    description="De novo spatial reconstruction of single-cell gene expression.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajewsky-lab/novosparc",
    license='MIT',
    install_requires=required_packages,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X"
    ]
)
