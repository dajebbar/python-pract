def mean_results(lst):
    return round(sum(lst) / len(lst), 2)

def from_file_to_list(file):
    res_note = []
    with open(file, 'r') as f:
        for note in f:
            res_note.append(float(note))
    
    return res_note


file = 'notes.txt'
mean = mean_results(from_file_to_list(file))
print(f'la moyenne des notes en python est : {mean}')