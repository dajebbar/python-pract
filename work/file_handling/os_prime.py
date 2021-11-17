# objet_fichier = open('text.txt', 'a')
# objet_fichier.write('hi fichier !\n')
# objet_fichier.write('Quel beautemps aujourd\'hui !\n')
# objet_fichier.close()

objet_fichier = open('text.txt', 'r')
print(objet_fichier.read(7))
print(objet_fichier.read(15))

objet_fichier.close()

