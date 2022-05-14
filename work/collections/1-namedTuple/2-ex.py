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
        print(f'{super().__str__()}\nID: {self.id}\nRole: {self.role}')


t1 = Trainee('ali', 'boubek', '20', '45-rt123', 'DLE')
t1
