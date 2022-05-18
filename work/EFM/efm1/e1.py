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
        return f'Firstname: {self._fname}\nLastname: {self._lname}\nidentityNum: {self._idy}'


class Vaccinated(Person):
    def __init__(self, fname=None, lname=None, idy=None, codeVaccin=None, dateVaccin=None):
        super().__init__(fname, lname, idy)
        self.__codeVaccin = codeVaccin
        self.__dateVaccin = dateVaccin
    
    def getCodeVaccin(self):
        return self.__codeVaccin
    def setCodeVaccin(self, cv):
        self.__codeVaccin = cv
    
    def getDateVaccin(self):
        return self.__dateVaccin
    def setDateVaccin(self, dv):
        self.__dateVaccin = dv
    
    def __str__(self):
        return f'{super().__str__()}\nVaccination code: {self.__codeVaccin}\nDate vaccination: {self.__dateVaccin}'
