# recursive fibinacci sequence
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-2) + fibo(n-1)

# fibonacci seq
def fib(n):
    if n < 2:
        return 1
    else:
        a = 1
        b = 1
        c = 1
        for i_ in range(2, n):
            c = a+ b
            a = b
            b = c
    return c

# print(fib(20))
# print(fibo(20))

# check given number if is fibonacci num
# input = int(input("giv a number >>> "))
# lst = []
# for i in range(input+1):
#     lst.append(fib(i))
# # print(lst)
# if input in lst:
#     print(True)
# else:
#     print(False)

# TODO
# A number is Fibonacci if and only if one or both of 
# (5*n^2 + 4) or (5*n^2 – 4) is a perfect square

def check_fibo(input):
    lst = []
    for i in range(input+1):
        lst.append(fib(i))
    # print(lst)
    if input in lst:
        print(True)
    else:
        print(False)

import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s ==  x

def is_fibonacco(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

for i in range(1, 11):
    if is_fibonacco(i) == True:
        print(f"{i} Fibonacci number")
    else:
        print(f'{i} Not Fibonacci number')




def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print i,"is a Fibonacci Number"
     else: 
         print i,"is a not Fibonacci Number "