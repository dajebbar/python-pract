from fileinput import filename
from p1 import Vendor
from collections import deque
import csv
from os import strerror

def get_vendor():
    print('--*** VENDORS ***--')
    n_vendor = int(input('Number of vendor(s)?>>> '))
    # data rows of csv file
    vend = deque()
    for item in range(n_vendor):
        print(f'--- INFO VENDOR {item+1} ---')
        v = Vendor(
            input('Code of vendor?>>> '),
            input('Adress of vendor?>> '),
            input('Commercial name?>>> ')
        )

        vend.append(v.vendors())
    
    # print(vend)
    
    # field names
    fields = ['code_vendor', 'adress', 'commercial_name',]
    # name of csv file
    filename = "vendor_file.csv"
    
    try:
        with open(filename, 'a') as f:
            csvwriter = csv.writer(f)
            # csvwriter.writerow(fields)
            csvwriter.writerows(vend)
    except Exception as e:
        print(strerror(e.erno))


if __name__=='__main__':
    get_vendor()


