def remove_hash(source, destination):
    s = open(source, 'r')
    d = open(destination, 'w')
    while True:
        line = s.readline()
        if line == '':
            break
        if line[0] != '#':
            d.write(line)

    d.close()
    s.close()
    print('done!')
    return

        
source = 'text.txt'
destination = 'foo'
remove_hash(source, destination)
