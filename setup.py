# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools.command.test import test as TestCommand

install_requires = []
try:
    import argparse
except ImportError:
    install_requires.append('argparse')

def latest_version_number():
    """It will open the changelog and return the most
    recent version on it. The first line respect the following format:

        X.Y, YYYY-MM-DD -- Some intro

    Where "X.Y" is the version number, defined according to PEP 386[1]

    [1]: http://www.python.org/dev/peps/pep-0386/
    """
    with open('CHANGELOG.rst') as f:
        version_and_date = f.readline().split('--')[0]

        return version_and_date.split(',')[0]


class Tox(TestCommand):
    """Boilerplate code from
    http://tox.readthedocs.org/en/latest/example/basic.html#integration-with-setuptools-distribute-test-commands
    """

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='Owl',
    author='Lucas S. Magalhães',
    author_email='me@lsmagalhaes.com',
    description='It helps you configure anything',
    long_description='long_description',
    license='Apache Software License',
    version=latest_version_number(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    packages=['owl'],
    install_requires=install_requires,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    scripts=['bin/owl']
)
