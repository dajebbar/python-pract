# https://www.marinetraffic.com/en/ais/home/centerx:-12.0/centery:25.0/zoom:4
# extended and abbreviated:
# have exactly the same number of entries;
# and correspond to the same ships;
# but naturally at different times;
# and not necessarily in the same order.

from collections import defaultdict


def merge(extended, abbreviated):
    """[Function that return a dictionary from merged lst]

    Args:
        extended ([list]): [extended]
        abbreviated ([list]): [abbreviated]
    """
    info = defaultdict(tuple)
    a_e = []

    for item in abbreviated:
        id_abr, *t = item
        a_e.append(tuple(t))

    for index, item in enumerate(extended):
        id_ext, *tt, name, code = item[:-2]
        info[id_ext] = [name, code, tuple(tt), a_e[index]]
    return info
