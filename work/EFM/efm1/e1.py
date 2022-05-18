class Person:
    def __init__(self, fname=None, lname=None, idy=None):
        self._fname = fname
        self._lname = lname
        self._idy = idy
    
    @property
    def fname(self):
        return self._fname
    @fname.setter
    def fname(self, fname):
        self._fname = fname
    
    @property
    def lname(self):
        return self._lname
    @lname.setter
    def lname(self, lname):
        self._lname = lname
    
    @property
    def idy(self):
        return self._idy
    @idy.setter
    def idy(self, idy):
        self._idy = idy
    
    def __str__(self):
        return f'Firstname: {self._fname} - Lastname: {self._lname} - identityNum: {self._idy}'
    
