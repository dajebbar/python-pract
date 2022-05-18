import csv


def write_files(filename):
    with open(filename, 'a') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(['fname', 'lname', 'mark'])
        csv_writer.writerow(['ahmadi', 'alaa', '15.5'])
        csv_writer.writerow(['khalidi', 'hind', 11])
        csv_writer.writerow(['ibrahimi', 'layla', 16])
    
    print('Done!')

filename='marks.csv'
write_files(filename)