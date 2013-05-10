from csort import __version__
from setuptools import setup

setup(
    name='csort',
    py_modules=['csort'],
    scripts=["csort"],
    version=__version__,
    license='BSD',
    platforms=['POSIX', 'Windows'],
    description='sort columns',
    author='Toshiyuki Takahashi',
    author_email='t.toshi.0412 at gmail.com',
    url='https://github.com/tototoshi/csort',
    keywords=['tsv'],
    classifiers = [
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities ",
        "Topic :: Software Development",
        ],
    long_description='Sort columns',
    install_requires = ["argparse"],
    test_suite = 'test_csort.suite'
    )
