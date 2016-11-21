from setuptools import setup, find_packages


packages = find_packages()

setup(
  name='pactest',
  version='1.0.0',
  zip_safe=True,
  packages=packages,
  include_package_data=True,
  package_data={
    'pactest' : ['data/subfolder/*']
  }
)