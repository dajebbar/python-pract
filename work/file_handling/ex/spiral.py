import math
import pickle


def cartesian_coordinates(theta=0, radius=.5, step=.1):
    """"""
    x_A = []
    y_A = []

    for _ in range(13):
        for _ in range(13):
            x_A.append(round(math.cos(theta) * radius, 5))
            y_A.append(round(math.sin(theta) * radius, 5))

            radius += step
        theta += step

    return list(zip(x_A, y_A))


def to_file(lst):
    with open('spiral.dat', 'w', encoding='utf8') as f:
        for x, y in lst:
            f.write(str(x) + '  ' + str(y) + '\n')

        print("spiral.dat done!")

def to_pickle(lst):
    coor = dict(lst)
    with open('spiral', 'wb') as f:
        pickle.dump(coor, f)
    print("pickle done!")


coor = cartesian_coordinates()
# to_file(coor)
# to_pickle(coor)

with open('spiral', 'rb') as f:
    # for coor in f:
    print(pickle.load(f))




