"""Module multiply contenant la fonction tables"""


def tables(nbr, max=10):
    """fonction tables qui prend deux arguments"""
    res = ""
    for item in range(max):
        res += f"{nbr} * {item+1} = {nbr*(item+1)}\n"
    return res

# test de la fonction tables dans le même module

if __name__ == "__main__":
    res = tables(5, 3)
    print(res)