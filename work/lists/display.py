def display_str(*args, sep=' ', lim='\n'):
    # convert elmts of tuple in string and
    # convert tuple to list
    arg = [str(item) for item in args]
    # add separator sep
    arg = sep.join(arg)
    # add lim
    arg += lim

    print(arg, end='')


display_str('October', 20, 2021)
