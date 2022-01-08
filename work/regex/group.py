import re
from func import import_text


string = import_text()

# pattern = re.compile(r'.+\s(.+ex).+(\d\d\s.+).')
pattern = re.compile(r'.+\s(.+ex).+(\d\d\s.+).')
# pattern = re.compile('index')

matches = re.search(pattern, string)
# print(string)
if matches:
    print(matches.groups())
    print(matches.group(1))
    print(matches.group(2))
    
else:
    print(None)