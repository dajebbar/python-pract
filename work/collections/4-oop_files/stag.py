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
    
    def __str__(self):
        return f'code:{self.__code} fname:{self.__fname} lname:{self.__lname} mark:{self.__mark}'
    
    def save_to_file(self, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'code:{self.__code} fname:{self.__fname} lname:{self.__lname} mark:{self.__mark}')
        print('done!')


if __name__=='__main__':
    # s1 = Trainee('id1111', 'alan', 'tores', 12.75)
    # s1.save_to_file('trainees.txt')
    with open('trainees.txt', 'r') as f:
        v = []
        l = {'code':[], 'first_name':[], 'last_name':[], 'mark':[]}
        for line in f.readlines():
            v.append(line.split(' '))
        
        for item in v:
            l['code'].append(item[0][item[0].index(':')+1:])
            l['first_name'].append(item[1][item[1].index(':')+1:])
            l['last_name'].append(item[2][item[2].index(':')+1:])
            l['mark'].append(float(item[-1][item[3].index(':')+1:-1]))
    print(l)