def bissextile(year):
    year_checked(year)
    res = ""
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        res = f"{year} is a leap year."
    else:
        res = f"{year} is not a leap year."

    return res


def year_checked(year):
    if len(str(year)) < 4:
        print(f"{year} is not a valid year.")


go = True


while go:

    try:
        year = int(input("Give a valid year >>> "))

    except ValueError as ve:
        print(ve)

    else:

        print(bissextile(year))

    res = input("Would you like to continue??[y/n] >>> ")
    if res == 'n' or res == 'N':
        go = False
