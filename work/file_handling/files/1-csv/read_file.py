import csv

def read_files(filename):
    with open(filename) as f:
        reader_csv = csv.reader(f)
        for line in reader_csv:
            print(line)

def read_dict(filename):
    with open(filename) as f:
        reader_csv = csv.DictReader(f)
        for line in reader_csv:
            print(line)


filename='combats.csv'
# read_files(filename)
read_dict(filename)