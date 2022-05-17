from p1 import Computer, Vendor
from collections import OrderedDict
from datetime import date

def get_computers():
    print('--*** Computers ***--')
    n_computers = int(input('Number of computer(s)?>>> '))
    computers= OrderedDict()

    for item in range(n_computers):
        print(f'--- INFO Computer {item+1} ---')
        c = Computer(
            input('Code of computer?>>> '),
            input('Brand of computer?>> '),
            date(input('year sell>>> '), input('month sell>>> '), input('day sell>>> ')),
            float(input('Price?>>> ')),
            Vendor(
                input('Code of vendor?>>> '),
                input('Adress of vendor?>> '),
                input('Commercial name?>>> ')
            )
        )

        computers[item+1] = c
    
    with open('comp_file.txt', 'a') as f:
        for item in computers:
            f.write(str(item))
    
    return computers