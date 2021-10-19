def bissextile(year):
    res = ""
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        res = f"{year} is a leap year."
    else:
        res = f"{year} is not a leap year."

    return res


if __name__ == "__main__":
    go = True

    while go:

        try:
            year = int(input("Give a valid year >>> "))
            if year <= 0 or len(str(year)) != 4:
                raise ValueError(
                    "Year should be positive and contains 4 digits")

        except ValueError as ve:
            print(ve)


        else:

            print(bissextile(year))

        res = input("Would you like to continue??[y/n] >>> ")
        if res == 'n' or res == 'N':
            go = False
