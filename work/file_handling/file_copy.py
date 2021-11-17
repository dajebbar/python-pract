def file_copied(source, destination):
    """[copy all text by 50 characters from source file to destination file]

    Args:
        source ([file]): [source file]
        destination ([file]): [destination file]
    """

    file_source = open(source, 'r')
    file_destination = open(destination, 'w')
    while True:
        txt = file_source.read(50)
        if txt == "":
            break
        file_destination.write(txt)
    
    file_destination.close()
    file_source.close()
    return

source = 'text.txt'
destination = 'zoo50'
file_copied(source, destination)

