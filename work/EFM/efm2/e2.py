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
    
