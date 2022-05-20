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
            print(f'grade must be in {(1,2,3)}')
    

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
        profiles = ['Front End', 'Back End', 'Full Stack']
        if  self._profile.title() in profiles:
             return self._profile
        else:
            print(f'Profile must be in {profiles}')
        
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
        if self._grade in (1,2,3):
            return self._grade
        else:
            print(f'grade must be in {1,2,3}')

    @grade.setter
    def grade(self, g):
        self._grade = g
    
    def salary(self):
        return self._grade * 3500
    
    def __str__(self):
        return f'ID:{self._idy}\nFname:{self.fnameI}\nLname:{self.lnameI}\nProfile:{self._profile}\nHDate:{self._hiringDate}\nGrade:{self._grade}'
    
class Team:
    def __init__(self):
        self.__cs = collections.deque()
    
    @property
    def cs(self):
        for item in self.__cs:
            return item
    @cs.setter
    def cs(self, c):
        self.__cs = c

    def add_cs(self, c):
        self.__cs.append(c)
    
    def remove_cs(self, idy):
        for c in self.__cs:
            if c.idy == idy:
                self.__cs.remove(c)
                return
        return f'the ID number {idy} does not exist!'

    def the_cs(self, idy):
        for c in self.__cs:
            if c.idy == idy:
                return c
        print(f'the ID number {idy} does not exist!')
        return None
    def __str__(self):
        l = ''
        for item in self.__cs:
            l += str(item) + '\n'
        return l

class TechLead(ComputerScientist):
    def __init__(self, idy, fname, lname, profile, hiring_date, grade, project_name=None, stuff=None):
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
    
    def __str__(self):
        return f'{super().__str__()}\nProject name:{self.__projectName}\nStuff:\n{self.__stuff}'


if __name__ == '__main__':
    tl1 = TechLead('123', 'kevin', 'lee', 'Full Stack', '2020-5-23', 2, 'ecom')
    cs1 = ComputerScientist('222', 'amendine', 'tiso', 'front end', '2018-3-25', 1)
    cs2 = ComputerScientist('333', 'ilan', 'dendo', 'back end', '2019-6-14', 3)

    team1 = Team()
    team1.add_cs(cs1)
    team1.add_cs(cs2)
    # print(team1.the_cs('222'))
    tl1.stuff = team1
    
    
    # print(team1.cs)
    # for item in team1:
    #     print(item)
    # print(tl1.stuff)

    # print(cs1)
    # print('***' * 9)
    # print(tl1)

    # print()
    # print('xxx' * 9)
    # team1.remove_cs('222')
    # tl1.stuff = team1.the_cs('222')
    # print(tl1)

    with open('techleaders.txt', 'a') as f:
        f.write(str(tl1) + '\n')
        print('done!')