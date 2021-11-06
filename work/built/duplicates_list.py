from collections import Counter
def catch_duplicates(lst):
    res = []
    data = Counter(lst)
    for k, v in data.items():
        if v  > 1:
            res.append(k)
    return res
    
    
# lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst = [-1, 1, -1, 8]

res = catch_duplicates(lst)
print(res)