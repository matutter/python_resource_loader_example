import pkg_resources
from os import path, pathsep
from errno import ENOENT


from loader import Loader, InvalidResourceError

loader = Loader(__name__, prefix='data')
data_path = 'subfolder/mydata.txt'
data_url = 'subfolder'

def test1():
  print 'loader.read'
  print loader.read(data_path)

def test2():
  print 'loader.open'
  fd = loader.open(data_path)
  print fd.read().strip()
  fd.close()

def test3():
  print 'loader.filename'
  uri = loader.filename(data_path)
  print 'resolved uri:', uri

def test4():
  print 'uri doesn\'t exist'
  try:
    uri = loader.filename('asd')
  except InvalidResourceError as e:
    print 'InvalidResourceError was thrown [GOOD]'
  except:
    raise

def test5():

  print 'loader.list'
  print loader.list(data_url)

def test6():
  print 'using loaders in submodules'
  from sub0 import test
  test()
    
def getTests():
  return [test1, test2, test3, test4, test5, test6]


if __name__ == "__main__":
  i = 0
  success = 0
  tests = getTests()
  for test in tests:
    i += 1
    try:
      print '-----', 'test', i, '-----'
      test()
      print '-----', 'test', i, 'SUCCESS', '-----'
      success += 1
    except Exception as e:
      print e
      print '-----', 'test', i, 'FAILED', '-----'

  print '{}/{} tests succeeded'.format(success, len(tests))