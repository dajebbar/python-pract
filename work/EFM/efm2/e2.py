import collections

class ComputerScientist:
    def __init__(self, idy=None, fnameI=None, lnameI=None, profile=None, hiring_date=None, grade=None):
        self._idy = idy
        self._fnameI = fnameI
        self._lnameI = lnameI
        profiles = ['Front End', 'Back End', 'Full Stack']
        if  profile.title() in profiles:
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
    
class Team:
    def __init__(self):
        self.cs = collections.deque()
    
    def add_cs(self, cs):
        self.cs.append(cs)
    
    def remove_cs(self, idy):
        for cs in self.cs:
            if cs.idy == idy:
                self.cs.remove(cs)
                return
        return f'the ID number {idy} does not exist!'

    def the_cs(self, idy):
        for cs in self.cs:
            if cs.idy == idy:
                return cs
        return f'the ID number {idy} does not exist!'

class TechLead(ComputerScientist):
    def __init__(self, idy, fname, lname, profile, hiring_date, grade, project_name, stuff):
        super().__init__(idy, fname, lname, profile, hiring_date, grade)
        self.__projectName = project_name
        self.__stuff = stuff

    @property
    def projectName(self):
        return self.__projectName
    @projectName.setter
    def projectName(self, pn):
        self.__projectName = pn
    
    @property
    def stuff(self):
        return self.__stuff
    @stuff.setter
    def stuff(self, s):
        self.__stuff = s
    
    def salary(self):
        return super().salary() + len(self.__stuff) * 800


if __name__ == '__main__':
    tl1 = TechLead('123', 'kevin', 'lee', )