import sqlite3
# path to DB
data_files = '/home/ehp/Documents/Python-codes/TeacherDuNet/gerard_swinnen_python/bdd/bd_test.sq3'
# connexion to DB
conn = sqlite3.connect(data_files)
# intermediaire temporary buffer between DB and connexion interface
cur = conn.cursor()
try:
    # request for creating members table in DB
    cur.execute("create table members(age integer, name text, height real)")

    # enter records to  members table
    cur.execute(
        "insert into members(age, name, height) values(4, 'Ali-Riad', 1.00)")
    cur.execute(
        "insert into members(age, name, height) values(33, 'Fatima-Zahra', 1.69)")
    cur.execute(
        "insert into members(age, name, height) values(38, 'Dajebbar', 1.83)")
except sqlite3.OperationalError:
    print("table already exists ")

# transfert data to DB
conn.commit()

# close cursor
cur.close()

# close connexion
conn.close()
