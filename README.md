# python_resource_loader_example
An example of loading package resources with pkg_resource.

The `Loader` class from `pactest.loader` module is an example of how to
use the `pkg_resource` library to read data from within a python egg or source distribution.

The `pactest.__main__` method runs a few "tests" to see if the imports succeed as a source
install and the `test/test.py` script checks if the egg install works the same.
