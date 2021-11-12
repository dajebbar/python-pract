def even_str(str):
    lst = []
    for i in str.split(' '):
        if len(i) % 2 == 0:
            lst.append(i)
    
    return ' '.join(lst)


str = "Hello guy it's a pleasure to see you"

print(even_str(str))