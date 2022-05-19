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
    
    # @property
    def getIdy(self):
        return self._idy
    # @idy.setter
    # def idy(self, idy):
    #     self._idy = idy
    
    def __str__(self):
        return f'Firstname: {self._fname}\nLastname: {self._lname}\nidentityNum: {self._idy}'


class Vaccinated(Person):
    def __init__(self, fname=None, lname=None, idy=None, codeVaccin=None, dateVaccin=None):
        super().__init__(fname, lname, idy)
        self.ation = codeVaccin
        self.__dateVaccination = dateVaccin
    
    def getCodeVaccin(self):
        return self.__codeVaccination
    def setCodeVaccin(self, cv):
        self.__codeVaccination = cv
    
    def getDateVaccin(self):
        return self.__dateVaccination
    def setDateVaccin(self, dv):
        self.__dateVaccination = dv
    
    def __str__(self):
        return f'{super().__str__()}\nVaccination code: {self.__codeVaccinaion}\nDate vaccination: {self.__dateVaccination}'


class Vaccine:
    def __init__(self, code_vaccine=None, name_vaccine=None, duration_between_2_dose=None):
        self.__codeVaccine = code_vaccine
        self.__nameVaccine = name_vaccine
        self.__durationBetween2Dose = duration_between_2_dose

    @property
    def codeVaccine(self):
        return self.__codeVaccine
    @codeVaccine.setter
    def codeVaccine(self, cv):
        self.__codeVaccine = cv
    
    @property
    def nameVaccine(self):
        return self.__nameVaccine
    @nameVaccine.setter
    def nameVaccine(self, nv):
        self.__nameVaccine = nv
    
    @property
    def durationBetween2Dose(self):
        return self.__durationBetween2Dose
    @durationBetween2Dose.setter
    def durationBetwwen2Dose(self, d):
        self.__durationBetween2Dose = d


    def __str__(self):
        return f'Vaccine code: {self.__codeVaccine}\nVaccine name: {self.__nameVaccine}\nDuration 2 Vdose: {self.__durationBetween2Dose}'


class Dose:
    def __init__(self, 
        dose_code=None, 
        vaccine=None, 
        vaccinated=None, 
        date_1st_dose=None,
        date_2nd_scheduled_dose = None,
        date_2nd_effective_dose = None
    ):
        self.__doseCode = dose_code
        self.__vaccine = vaccine
        self.__vaccinated = vaccinated
        self.__dateFirstDose = date_1st_dose
        self.__dateSecondScheduledDose = date_2nd_scheduled_dose
        self.__dateSecondEffectiveDose = date_2nd_effective_dose