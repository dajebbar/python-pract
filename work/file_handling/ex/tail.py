def check(file):
    tail = []
    with open(file) as f:
        for line in f:
            tail.append((line, len(line)))
    
    return max(tail)


line, len_line = check('tail.txt')

print(f'the large line is:\n{line}\nit has {len_line} words')


