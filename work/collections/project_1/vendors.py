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
    
    with open('vendor_file.csv', 'a') as f:
        writer = csv.writer(f)
        for v in vendors:
            writer.writerows(v)


if __name__=='__main__':
    get_vendor()


