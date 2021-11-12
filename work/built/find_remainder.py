def remainder(lst, n):
    multiply = 1
    for i in lst:
        multiply *= i
    
    return multiply % n

lst = [100, 10, 5, 25, 35, 14]
n = 11


# print(remainder(lst, n))

# ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c

def find_remainder(lst, lens, n):
    multiply = 1
    for i in range(lens):
        multiply = (multiply * (lst[i] % n) ) % n
    
    return multiply % n

lens = len(lst)

print(find_remainder(lst, lens, n))