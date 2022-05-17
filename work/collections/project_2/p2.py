def take_file():
    info = {'id': [], 'fname': [], 'lname': [], 'mark': []}
    v = []
    file_name = input('file link?>> ')
    with open(file_name, 'r') as f:
        for line in f.readlines():
            for chr in line:
                print(chr, end='')
            
            v.append(line.split(' '))
    return v
                
v = take_file()
l = {}
for item in v:
    l[f'{item[-3]} {item[-2]}'] = float(item[-1][:-1])

for k, v in l.items():
    if l[k] == max(l.values()):
        print(f'{k} has the max mark')


# print(l)