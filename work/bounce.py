def bounce(height):
    item = 0
    while item < 10:
        print(f"{item+1} {height}")
        item += 1
        height = (height * 3/5)


bounce(60.0)
