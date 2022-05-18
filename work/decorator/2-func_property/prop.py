class Employee:
    def __init__(self, code, dept, city):
        self.__code = code
        self.__dept = dept
        self.__city = city
    
    def get_code(self):
        return self.__code
    def set_code(self, x):
        self.__code=x
    
    def get_dept(self):
            return self.__dept
    def set_dept(self, x):
        self.__dept=x
    
    def get_city(self):
            return self.__city
    def set_city(self, x):
        self.__city=x


    def __str__(self):
        print(f'EmployeeID: {self.__code}\nDepartment: {self.__dept}\nCity: {self.__city}')
