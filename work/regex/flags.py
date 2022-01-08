import re
from func import import_text


string = import_text()
s = "Hello \n from \n Python!"


# pattern = re.compile(r'the', flags=re.I)
pattern = re.compile(r'.+', flags=re.S)


matches = re.search(pattern, s)

if matches:
    print(matches)
    
else:
    print(None)