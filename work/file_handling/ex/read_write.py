def check_file(file):
    try:
        f = open(file, 'r')
        f.close()
        return 1
    except FileNotFoundError:
        return 0


def read_file(file):
    """"""

    if not check_file(file):
        print("file doesn't exists!")

    else:
        with open(file) as f:
            for txt in f:
                print(txt)
    return


def write_file(file, txt):
    with open(file, 'a') as f:
        f.write(txt + '\n')

    return

if __name__== '__main__':
    enter = input("Saisir le nom du fichier:  ")
    mode = input(
        'taper [r] pour lire le fichier \ntaper [w] pour enregister dans le fichier:  ')[0]

    if mode == 'w' or mode == 'W':
        print('w mode')
        txt = input("texte à rajouté:  ")
        while txt != '':
            write_file(enter, txt)
            txt = input("texte à rajouté:  ")
            if txt == '':
                break

    elif mode == 'r' or mode == 'R':
        print("r mode")
        read_file(enter)

    else:
        print("Error")
