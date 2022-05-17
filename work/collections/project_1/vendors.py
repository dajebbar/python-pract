from p1 import Vendor
from collections import deque
import csv

def get_vendor():
    print('--*** VENDORS ***--')
    n_vendor = int(input('Number of vendor(s)?>>> '))
    vendors = deque()
    for item in range(n_vendor):
        print(f'--- INFO VENDOR {item+1} ---')
        v = Vendor(
            input('Code of vendor?>>> '),
            input('Adress of vendor?>> '),
            input('Commercial name?>>> ')
        )

        vendors.append(v)
    for elem in vendors:
        print(elem.split(': ')[1])
    
    # with open('vendor_file.csv', 'a') as f:
        
    #     for elem in vendors:
    #         writer = csv.writer(f)
    #         writer.writerow(elem)


if __name__=='__main__':
    get_vendor()


