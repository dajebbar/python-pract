def import_text():
    """function that open file and return content

    Returns:
        [string]: [have a text]
    """
    string = ""
    with open('strings.txt', 'r', encoding='utf-8') as f:
        for line in f.read().split('\n'):
            string += line + '\n'
    
    return string


# res = import_text()
# print(res)