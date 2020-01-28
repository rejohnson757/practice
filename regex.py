import re

message = 'Please call me at 757-358-4287'

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = regex.search(message)
print(mo.group())
