from collections import deque


D = deque(['Sam', 'bob', 'lee'])
D.append('lina')
D.append('memy')
print(D)
D.appendleft('lili')
print(D)