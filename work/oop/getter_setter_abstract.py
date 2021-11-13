from abc import ABC, abstractmethod


class GetterSetter(ABC):
    @abstractmethod
    def get_val(self):
        return
    
    @abstractmethod
    def set_val(self, input):
        return


class MyClass(GetterSetter):

    def __init__(self, val):
        self.__val = val

    def set_val(self, input):
        self.__val = input
    
    def get_val(self):
        return self.__val
    
    def __str__(self):
        return f"{self.__val}"


x = MyClass(7)
print(x.get_val())
x.set_val(-7)
print(x.get_val())