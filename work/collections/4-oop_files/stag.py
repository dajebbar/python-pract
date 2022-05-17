class Trainee:
    def __init__(self, code, fname, lname, mark):
        self.__code = code
        self.__fname = fname
        self.__lname = lname
        self.__mark = mark
    
    def get_code(self):
        return self.__code
    def set_code(self, x):
        self.__code= x
    
    def get_fname(self):
        return self.__fname
    def set_fname(self, x):
        self.__fname = x
    
    def get_lname(self):
        return self.__lname
    def set_lname(self, x):
        self.__lname = x
    
    def get_mark(self):
        return self.__mark
    def set_mark(self, x):
        self.__mark= x