import csv


def write_files(filename):
    with open(filename, 'a') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(['fname', 'lname', 'mark'])
        csv_writer.writerow(['ahmadi', 'alaa', '15.5'])
        csv_writer.writerow(['khalidi', 'hind', 11])
        csv_writer.writerow(['ibrahimi', 'layla', 16])
    
    print('Done!')

students = [
    {'id':11, 'fname':'ahmadi', 'lname':'alaa', 'mark':15.5,},
    {'id':22, 'fname':'khalidi', 'lname':'hind', 'mark':11,},
    {'id':33, 'fname':'ibrahimi', 'lname':'layla', 'mark':16,},
    {'id':44, 'fname':'idba', 'lname':'walaa', 'mark':7.3,},
]

def write_dict(filename):
    with open(filename, 'a') as f:
        csv_writer = csv.DictWriter(delimiter=',', fieldnames=students[0].keys())
        csv_writer.writeheader()
        for line in students:
            csv_writer.writerow(line)
    print('done!!')


# filename='marks.csv'
# write_files(filename)

filename='marks_dict.csv'
write_dict(filename)