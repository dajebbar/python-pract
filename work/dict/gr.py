from collections import defaultdict


def graph_dict(link):
    d = defaultdict(list)
    with open(link) as file:
        for line in file:
            start, middle, end = line.split()
            d[start].append((end, int(middle)))
    return d


link = 'graph.txt'
for k, v in graph_dict(link).items():
    print(f"{k} {v}")



