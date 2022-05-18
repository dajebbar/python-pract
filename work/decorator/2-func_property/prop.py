class Employee:
    def __init__(self, code, dept, city):
        self.__code = code
        self.__dept = dept
        self.__city = city
    
    def __str__(self):
        print(f'EmployeeID: {self.__code}\nDepartment: {self.__dept}\nCity: {self.__city}')
