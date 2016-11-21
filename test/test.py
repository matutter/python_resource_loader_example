


print 'testing...'


from pactest import getTests

tests = getTests()

i = 0
success = 0
for test in tests:
  i += 1
  try:
    print '-----', 'test', i, '-----'
    test()
    success += 1
    print '-----', 'test', i, 'SUCCESS', '-----'
  except Exception as e:
    print '-----', 'test', i, 'FAILED', '-----'
    print e

  print '{}/{} tests succeeded'.format(success, len(tests))