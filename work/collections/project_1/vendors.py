from p1 import Vendor
from collections import deque
import csv
from os import strerror

def get_vendor():
    print('--*** VENDORS ***--')
    n_vendor = int(input('Number of vendor(s)?>>> '))
    vend = deque()
    for item in range(n_vendor):
        print(f'--- INFO VENDOR {item+1} ---')
        v = Vendor(
            input('Code of vendor?>>> '),
            input('Adress of vendor?>> '),
            input('Commercial name?>>> ')
        )

        vend.append(v.vendors())
    
    print(vend)

    
    
    # try:
    #     with open('vendor_file.csv', 'a') as f:
            
    #         for elem in vendors:
    #             writer = csv.writer(f)
    #             writer.writerow(elem)
    # except Exception as e:
    #     print(strerror(e.erno))


if __name__=='__main__':
    get_vendor()


