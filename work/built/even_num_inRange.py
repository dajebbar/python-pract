def even(start, end):
    even_lst = []

    for i in range(start, end+1):
        if i % 2 == 0:
            even_lst.append(i)
    
    return even_lst

print(even(4, 15))
print(even(8, 11))
