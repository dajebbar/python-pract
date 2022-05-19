import collections

class ComputerScientist:
    def __init__(self, idy=None, fnameI=None, lnameI=None, profile=None, hiring_date=None, grade=None):
        self._idy = idy
        self._fnameI = fnameI
        self._lnameI = lnameI
        profiles = ['FrontEnd', 'BackEnd', 'FullStack']
        if  profile in profiles:
            self._profile = profile
        else:
            print(f'Profile must be in {profiles}')
        self._hiringDate = hiring_date
        if grade in [1, 2, 3]:
            self._grade = grade
        else:
            print(f'grade must be in {1,2,3}')
    

    @property
    def idy(self):
        return self._idy
    @idy.setter
    def idy(self, idy):
        self._idy = idy
    
    @property
    def fnameI(self):
        return self._fnameI
    @fnameI.setter
    def fnameI(self, fn):
        self._fnameI = fn
    
    @property
    def lnameI(self):
        return self._lnameI
    @lnameI.setter
    def lnameI(self, ln):
        self._lnameI = ln
    
    @property
    def profile(self):
        return self._profile
    @profile.setter
    def profile(self, pr):
        self._profile = pr
    
    @property
    def hiringDate(self):
        return self._hiringDate
    @hiringDate.setter
    def hiringDate(self, hd):
        self._hiringDate = hd
    
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, g):
        self._grade = g
    
    def salary(self):
        return self._grade * 3500
    
    def __str__(self):
        return f'ID:{self._idy}\nFname:{self.fnameI}\nLname:{self.lnameI}\nProfile:{self._profile}\nHDate:{self._hiringDate}\nGrade:{self._grade}'
    
    