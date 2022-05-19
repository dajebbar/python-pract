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
    def __init__(self, fname, lname, idy, codeVaccin, dateVaccin):
        super().__init__(fname, lname, idy)
        self.__codeVaccination = codeVaccin
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

from copy import deepcopy
class Vaccine:
    def __init__(self, code_vaccine, name_vaccine, duration_between_2_dose):
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
        dose_code, 
        vaccine, 
        vaccinated, 
        date_1st_dose,
        date_2nd_scheduled_dose,
        date_2nd_effective_dose
    ):
        self.__doseCode = dose_code
        self.__vaccine = vaccine
        self.__vaccinated = vaccinated
        self.__dateFirstDose = date_1st_dose
        self.__dateSecondScheduledDose = date_2nd_scheduled_dose
        self.__dateSecondEffectiveDose = date_2nd_effective_dose
    

    @property
    def doseCode(self):
        return self.__doseCode
    @doseCode.setter
    def doseCode(self, dc):
        self.__doseCode = dc
    
    @property
    def vaccine(self):
        return self.__vaccine
    @vaccine.setter
    def vaccine(self, v):
        self.__vaccine = v
    
    @property
    def vaccinated(self):
        return self.__vaccinated
    @vaccinated.setter
    def vaccinated(self, v):
        self.__vaccinated = v
    
    @property
    def dateFirstDose(self):
        return self.__dateFirstDose
    @dateFirstDose.setter
    def dateFirstDose(self, d):
        self.__dateFirstDose = d
    
    @property
    def dateSecondScheduledDose(self):
        return self.__dateSecondScheduledDose
    @dateSecondScheduledDose.setter
    def dateSecondScheduledDose(self, dssd):
        self.__dateSecondScheduledDose = dssd
    
    @property
    def dateSecondEffectiveDose(self):
        return self.__dateSecondEffectiveDose
    @dateSecondEffectiveDose.setter
    def dateSecondEffectiveDose(self, dsed):
        self.__dateSecondEffectiveDose = dsed
    

    def __str__(self):
        return f'Code of dose: {self.__doseCode}\nVaccin: {self.__vaccine.__str__()}\nVaccinated: {self.__vaccinated.__str__()}\nDate of 1st dose : {self.__dateFirstDose}\nScheduled dose: {self.__dateSecondScheduledDose}\nEffective dose: {self.__dateSecondEffectiveDose}'

import collections
class VaccinationCenter:
    def __init__(self, center_name=None, center_adress=None):
        self.__centerName = center_name
        self.__centerAdress = center_adress
        self.__vaccins = collections.deque()
        self.__vaccinated = collections.deque()
        self.__doses = collections.deque()
    

    @property
    def centerName(self):
        return self.__centerName
    @centerName.setter
    def centerName(self, cn):
        self.__centerName = cn
    
    @property
    def centerAdress(self):
        return self.__centerAdress
    @centerAdress.setter
    def centerAdress(self, ca):
        self.__centerAdress = ca
    
    def find_vaccine(self, code_vaccine):
        for vaccin in self.__vaccins:
            if vaccin.codeVaccine == code_vaccine:
                return vaccin
            else:
                return f'The vaccine with code num {code_vaccine} is not found!'
    
    def add_vaccine(self, vaccine):
        self.__vaccins.append(vaccine)
    
    def delete_vaccine(self, code_vaccine):
        for vaccin in self.__vaccins:
            if vaccin.codeVaccine == code_vaccine:
                self.__vaccins.pop(vaccin)
    

    def find_vaccinated(self, code_vaccinated):
        for vaccinated in self.__vaccinated:
            if vaccinated.getCodeVaccin() == code_vaccinated:
                return vaccinated
            
            else:
                return f'The vaccinated with code num {code_vaccinated} is not found!'
    
    def add_vaccinated(self, vaccinated):
        self.__vaccinated.append(vaccinated)
    

    def add_dose(self, dose):
        self.__doses.append(dose)

    


if __name__=='__main__':
    # p1 = Person('kevin', 'lee', 'E125')
    # print(p1)
    vaccine1 = Vaccine('vac-123', 'Pfizer', 21)
    vaccine2 = deepcopy(vaccine1)
    print(f'Vac1 info: {vaccine1}')
    print(f'Vac2 info: {vaccine2}')