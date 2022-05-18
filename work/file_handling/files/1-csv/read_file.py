import csv

def read_files(filename):
    with open(filename) as f:
        reader_csv = csv.reader(f)
        for line in reader_csv:
            print(line)


filename='combats.csv'
read_files(filename)