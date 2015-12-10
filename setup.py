import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    user_options = [
        ('pytest-args=', 'a', 'Arguments for pytest'),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_target = []
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

version = '0.1'

setup_requires=[
    'pytest'
]
install_requires=[
    'requests',
]
tests_require=[
    'pytest-xdist',
    'pytest-timeout',
    'pytest'
]

setup(name='pytest_sample',
      version=version,
      description="Sample project for the article",
      long_description=open(
          os.path.join(
              os.path.dirname(__file__),
              'README.rst')).read(),
      classifiers=[],
      keywords='',
      author='FGtatsuro',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'tests', 'results']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=setup_requires,
      install_requires=install_requires,
      tests_require=tests_require,
      cmdclass={'test': PyTest},
)
