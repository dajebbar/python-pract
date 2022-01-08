import re
from func import import_text


string = import_text()
# pattern = re.compile(r'\d[^\.]{1,4}')
pattern = re.compile(r'[A-Z]{2,}')
matches = pattern.subn('INDEX', string)
# print(matches, len(matches))

print(matches[1])
