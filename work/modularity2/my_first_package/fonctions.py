"""Module multiply contenant la fonction tables"""


def table(nbr, max=10):
    """fonction tables qui prend deux arguments"""
    res = ""
    for item in range(max):
        res += f"{nbr} * {item+1} = {nbr*(item+1)}\n"
    return res

# test de la fonction tables dans le même module


if __name__ == "__main__":
    res = table(15, 5)
    print(res)
