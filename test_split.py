import re

namespace = 'root/sub'

print re.split(r'\.|\/|\\', namespace)[0]