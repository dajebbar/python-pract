from collections import deque


D = deque(['Sam', 'bob', 'lee'])
D.append('lina')
D.append('memy')
print(D)
D.appendleft('lili')
print(D)
D.pop()
print(D)
D.popleft()
print(D)
# D.clear()
# print(D)
D.extend(['ketty', 'boby'])
print(D)