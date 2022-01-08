import re

string = "I like play guitare. every night I play GUITARE!."

# req = re.findall(r"guitare", string)
# pattern = re.compile(r"guitare", flags=re.IGNORECASE)
# matches = pattern.findall(string)


# pattern_1 = re.compile(r"\.")
# matches = pattern_1.finditer(string)

# # cnt = 0
# for match in matches:
#     print(match)
#     cnt += 1
# print(cnt, len(string))

sentence = '''
The STOXX Europe 600 Index is derived from the STOXX Europe 
Total Market Index (TMI) and is a subset of the STOXX Global 1800 
Index. With a fixed number of 600 components, the STOXX Europe 600 
Index represents large, mid and small capitalization companies across 
17 countries of the European region: Austria, Belgium, Denmark, Finland, 
France, Germany, Ireland, Italy, Luxembourg, the Netherlands, Norway, Poland, 
Portugal, Spain, Sweden, Switzerland and the United Kingdom.

555-666-7777
112.223.3334
528*587*9824
800-578-2145
900-203-4060

cat
mat
pat
bat

Mr. Ali
Mr riad

Ms Mina
Mrs. Robinson
Mr. T

'''
# pattern = re.compile(r'\d{1,4}')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')

string = "Start saying Ha HaHa!"

# pattern = re.compile(r'\bHa\b')
# pattern = re.compile(r'^Star')
# pattern = re.compile(r'!$')
# pattern = re.compile(r'(\d{3}.\d{3}.\d{4})')
pattern = re.compile(r'(\d{3}[-.]\d{3}[-.]\d{4})')
# pattern = re.compile(r'([8|9]00[-.]\d{3}[-.]\d{4})')
# pattern = re.compile(r'[c|p|m]at')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'Mr\.?\s.+')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Za-z]\w*')

# matches = re.finditer(pattern, sentence)
# matches = re.findall(pattern, sentence)
# for match in matches:
#     print(match)

# pattern = re.compile(r'[89]00[.-]\d{3}[-.]\d{4}')
# pattern = re.compile(r'([a-zA-Z0-9\.\-+_])+@([a-zA-Z\.\-])+\.([a-zA-Z]){2,5}')

# urls = '''
#     https://www.google.com
#     http://coreyms.com
#     https://youtube.com
#     https://www.nasa.gov
#     dajebbar.free.fr 
# '''
# pattern = re.compile(r'(https?://(www\.)?)?([a-zA-Z0-9_\-\.+]+)(\.[a-zA-Z]{2,5})')
# subbed_url = pattern.sub(r'\3\4', urls)
# print(subbed_url)


# sentence = ""
# cnt = 0

# with open('urls.txt', 'r', encoding='utf-8') as f:
#     for line in f.read().split('\n'):
#         sentence += line + "\n"

# # print(sentence)

# matches = re.finditer(pattern, sentence)
# for match in matches:
#     print(match.group(4))
#     cnt += 1
# print(cnt)



string_exple = '''
Jessica is 15 years old, Daniel is 27 years old,
but Buizo is 3 years old, and me Dajebbar 38 years old.
'''

age_pattern = re.compile(r'\d{1,2}')
# ages = re.finditer(age_pattern, string_exple)
# for age in ages:
#     print(age)
print('*'*50)
name_pattern = re.compile(r'[A-Z][a-z]*')
# names = re.finditer(name_pattern, string_exple)
# for name in names:
#     print(name)

ages = re.findall(age_pattern, string_exple)
names = re.findall(name_pattern, string_exple)

age_name = {name: age for name, age in zip(names, ages)}
print(age_name)