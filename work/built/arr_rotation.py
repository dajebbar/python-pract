def arr_rotation(lst, n_size, d_elem=0):
    n_size = len(lst)
    elem_catched = []

    if d_elem > n_size:
        return 0
    
    else:
        for i in lst[:d_elem]:
            elem_catched.append(i)
            lst.remove(i)
    return lst + elem_catched

lst = [1, 2, 3, 4, 5, 6]
n = len(lst)
d = 2

res = arr_rotation(lst, n, d)
print(res)
        


