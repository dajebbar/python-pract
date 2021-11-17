import pickle

a, b, c = 27, 12.96, [5, 4.83, "René"]
my_dict = {'a': a, 'b': b, 'c': c,}
with open('bar', 'wb') as file:
    pickle.dump(my_dict, file)
    

with open('bar', 'rb') as file:
    j = pickle.load(file)

print(j)