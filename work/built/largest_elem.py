def largest_elem(lst):
    max = 0
    for i in lst:
        if i > max:
            max = i
    return max

lst = [100,-20, 0, -1, 7]
print(largest_elem(lst))