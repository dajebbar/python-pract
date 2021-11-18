import sqlite3


path = "/home/ehp/Documents/Python-codes/TeacherDuNet/gerard_swinnen_python/bdd/music_db/music_db.db"
data_comp = []
data_works = []

def insert_comp_into_db():
    data = []

    print("how many compositors will be added to the db?")
    comp_cnt = int(input())

    for comp in range(comp_cnt):
        print(f"enter the {comp+1} compositor info? ")
        try:
            name = input("name? ")
            yr_birth = int(input("year_of_birth? "))
            yr_death = int(input("year of death? "))
            if yr_birth >= yr_death:
                print("Error year of death must be grater than year of birth")
                yr_death = int(input("year of death? "))
            data.append((name, yr_birth, yr_death))
        except ValueError as e:
            print("e")

    return data


def insert_works_into_db():
    data = []

    print("how many works will be added to the db?")
    works_cnt = int(input())

    for work in range(works_cnt):
        print(f"enter the {work+1} work info? ")
        try:
            name = input("name? ")
            title = input("title? ")
            duration = int(input("duration? "))
            interpr = input("interpr? ")
            data.append((name, title, duration, interpr))
        except ValueError as e:
            print("e")

    return data


data_comp = insert_comp_into_db()
data_works = insert_works_into_db()

with sqlite3.connect(path) as conn:
    cur = conn.cursor()
    try:
        cur.executescript("""
            DROP TABLE IF EXISTS compositors;
            CREATE TABLE compositors(
                comp TEXT,
                year_of_birth INT,
                year_of_death INT
                );

            DROP TABLE IF EXISTS works;
            CREATE TABLE works(
                comp TEXT,
                title TEXT,
                duration INT,
                interpr TEXT
                );"""
                        )
        cur.executemany(
            "INSERT INTO compositors(comp, year_of_birth, year_of_death) VALUES (?,?,?)", data_comp)
        cur.executemany(
            "INSERT INTO works(comp, title, duration, interpr) VALUES (?,?,?,?)", data_works)
    except sqlite3.OperationalError as e:
        print(e)

    # else:
    print("Done!")
