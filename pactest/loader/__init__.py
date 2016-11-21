from errno import ENOENT
from os import pathsep
from re import split
from pkg_resources import resource_exists, \
  resource_filename, \
  resource_stream, \
  resource_string, \
  resource_listdir

"""
WARNING: If the security warning is printed for user installation it may 
be corrected with ``` chmod g-wx,o-wx ~/.python-eggs ```

@typedef InvalidResourceError
@extends Exception

@param uri {String} The URI which was requested within the given loader's
that did not exist or was malformed.
"""
class InvalidResourceError(Exception):
  
  def __init__(self, namespace, requested_uri):
    self.namespace = namespace
    self.requested_uri = requested_uri
    self.message = 'Resource does not exist or is declared incorrectly'
    self.errno = ENOENT
    super(InvalidResourceError, self).__init__(self.message)

  def __str__(self):
    return '{}({}), "{}" of {}'.format(self.message, self.errno, self.requested_uri, self.namespace)

  def __repr__(self):
    return self.__str__()

"""
@typedef Loader
@extends object

@param namespace {String} The namespace within the package (relative to the package root)
to load resources from. Using the magic variable __name__ is suggested as when the script
is run as "__main__" it will load the most recent local resources instead of the cached 
egg resources.
@param prefix {String} Set a prefix for all URIs. Use a prefix if resources are centrally
located in a single place the uri's will be prefixed automatically by the loader.
"""
class Loader(object):

  def __init__(self, namespace, **opts):
    self.namespace = namespace
    self.prefix = opts.get('prefix', '')
    self.local = opts.get('local', False)

    if not self.local:
      self.namespace = split(r'\.|\\|\/', self.namespace)[0]

  def _resolve(self, uri):
    resource_uri = '/'.join([self.prefix] + uri.split(pathsep))
    ns = self.namespace

    if not resource_exists(ns, resource_uri):
      raise InvalidResourceError(ns, resource_uri)

    return ns, resource_uri

  """
  Read entire contents of resource. Same as open('path...').read()
  @param uri {String} URI of the resource.
  """
  def read(self, uri):
    ns, uri = self._resolve(uri)
    return resource_string(ns, uri) 

  """
  Open a file object like handle to the resource. Same as open('path...')
  @param uri {String} URI of the resource.
  """
  def open(self, uri):
    ns, uri = self._resolve(uri)
    return resource_stream(ns, uri)

  """
  Return the "most correct" filename for a resource. Same as os.path.normpath('path...')
  @param uri {String} URI of the resource.
  """
  def filename(self, uri):
    ns, uri = self._resolve(uri)
    return resource_filename(ns, uri)

  """
  Return a list of all resources within the given URL
  @param url {String} URL of the resources.
  """
  def list(self, url):
    ns, uri = self._resolve(url)
    return map(lambda x: url+'/'+x,resource_listdir(ns, uri))
