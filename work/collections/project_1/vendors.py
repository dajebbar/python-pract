from p1 import Vendor
import json

def get_vendor():
    print('--*** VENDORS ***--')
    n_vendor = int(input('Number of vendor(s)?>>> '))
    vendors = []
    for item in range(n_vendor):
        print(f'--- INFO VENDOR {item+1} ---')
        v = Vendor(
            input('Code of vendor?>>> '),
            input('Adress of vendor?>> '),
            input('Commercial name?>>> ')
        )

        vendors.append(v)
    
    with open('vendor_file.json', 'a') as f:
        json.dump(vendors, f)



