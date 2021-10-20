def comma_decimal(num):
    """Function taking a float as a parameter and returning a character string 
    representing the truncation of this number. The floating part must have a 
    maximum length of 3 characters. In addition, we will replace the decimal 
    point by the comma
    """
    num_to_lst = list(str(num))
    three_digits = num_to_lst.index('.')+4
    num_trancate = num_to_lst[:three_digits]
    lst_to_str = "".join(num_trancate)
    comma = ','.join(lst_to_str.split('.'))
    return comma


def comma_decimal1(num):
    """Function taking a float as a parameter and returning a character string 
    representing the truncation of this number. The floating part must have a 
    maximum length of 3 characters. In addition, we will replace the decimal 
    point by the comma
    """

    if type(num) is not float:
        raise TypeError("The expected parameter must be a float!!")

    num = str(num)
    int_part, float_part = num.split('.')

    return ','.join([int_part, float_part[:3]])


try:
    num = float(input("Give a digit number: >>> "))
except ValueError:
    print('Could not convert string to float')
else:
    res = comma_decimal1(num)
    print(res)
