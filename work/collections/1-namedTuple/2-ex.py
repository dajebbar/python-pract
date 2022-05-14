from collections import namedtuple

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def __str__(self):
        return f'First name: {self.fname}\nLast name: {self.lname}\nAge: {self.age}'


class Trainee(Person):
    def __init__(self, fname, lname, age, id, role):
        super().__init__(fname, lname, age)
        self.id = id
        self.role = role
    
    def __str__(self):
        return f'{super().__str__()}\nID: {self.id}\nRole: {self.role}'


t1 = Trainee('ali', 'boubek', '20', '45-rt123', 'DLE')
p1 = Person('fz', 'lx', '15')
p2 = Person('krm', 'xml', 25)
# print(t1)

L = namedtuple('Per_train', ['Per', 'Train'])
l = L((p1, p2), t1)
# print(l)

for p in l.Per:
    print(p)
    print('-**-'* 5)

print(l.Train)
