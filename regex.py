import re

message = 'Please call me at 555-555-5555'

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = regex.search(message)
print(mo.group())
