def occurance_cnt(lst):
    occurance = {}
    for i in lst:
        occurance[i] = lst.count(i)
    
    return occurance


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# res = occurance_cnt(lst)
# print(res)
# print(res[10])
# i = 16
# if i in res.keys():
#     print(res[16])
# else:
#     print(None)

# Using Counter()

from collections import Counter

data = Counter(lst)
i = 7
print(data)
print(data[i])
i = 16
print(data[i])

key_more_1 = [k for k,v in data.items() if v > 1]
print(key_more_1)