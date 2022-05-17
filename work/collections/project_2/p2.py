def take_file():
    v = []
    l = {}
    file_name = input('file link?>> ')
    with open(file_name, 'r') as f:
        for line in f.readlines():
            for chr in line:
                print(chr, end='')
            
            v.append(line.split(' '))
    
    for item in v:
        l[f'{item[-3]} {item[-2]}'] = float(item[-1][:-1])

    for k, v in l.items():
        if l[k] == max(l.values()):
            print(f'{k} has the max mark')
                

take_file()




# print(l)