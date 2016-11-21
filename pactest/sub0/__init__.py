
from pactest.loader import Loader 



def test():
  loader = Loader(__name__, prefix='data')
  data_path = 'subfolder/mydata.txt'
  data_url = 'subfolder'
  print 'loader.read'
  print loader.read(data_path)


