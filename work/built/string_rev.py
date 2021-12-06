my_string = ('Découpez une grande chaîne en fragments de 5 caractères chacun.'
'Rassemblez ces morceaux dans l’ordre inverse. La chaîne doit pouvoir contenir des caractères accentués.')
fragment_5 = my_string[:6]
lst = []
for index, _ in enumerate(my_string):
    if not index % 5:
        lst.append(''.join(sorted(my_string[index:index+5])))

print(lst)
