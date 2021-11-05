def add_hat(dic):
    """[Adding hat if cat doesn't have one or remove it]

    Args:
        dic ([dict]): [contains all cats with and without hats]
    """
    for cat, hat in dic.items():
        if hat == 0:
            dic.update({cat: 1})

        else:
            dic.update({cat: 0})
       


def check_odd_cat(dic):
    """[Adding hat if pos of cat was even otherwise remove it]

    Args:
        dic ([dict]): [contains all cats with and without hats]
    """
    for index, item in enumerate(dic.items()):
        item = list(item)
        if index % 2 == 0:
            item[-1] = 1
        else:
            item[-1] = 0

        dic.update({item[0]: item[-1]})

        # print(index, list(item))


def check_3_cat(dic):
    """[Adding hat if pos of cat was multiple of 3 otherwise remove it]

    Args:
        dic ([dict]): [contains all cats with and without hats]
    """
    for index, item in enumerate(dic.items()):
        item = list(item)
        if index % 3 == 0:
            item[-1] = 1
        else:
            item[-1] = 0

        dic.update({item[0]: item[-1]})


d = {
    "kiki": 0,
    "mimi": 0,
    "lulu": 1,
    "qsti": 0,
    "ona":  0,
    "fofa": 1,
}

# add_hat(d)
# print(d)

# check_odd_cat(d)
# print(d)
