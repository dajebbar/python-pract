def admis(source, destination):
    with open(source) as fs, open(destination, 'w') as fd:
        for note in fs:
            if 20 >= float(note) >= 10:
                fd.write(note.strip() + ' ' + 'admis' + '\n')
            elif float(note) < 10:
                fd.write(note.strip() + ' ' + 'recalé' + '\n')
            else:
                fd.write(note.strip() + ' ' + 'Abbérente' + '\n')
    
    print('Done!')
    return


source = 'notes.txt'
destination = 'notes2.txt'

admis(source, destination)