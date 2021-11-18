import sqlite3
# path to DB
data_files = '/home/ehp/Documents/Python-codes/TeacherDuNet/gerard_swinnen_python/bdd/bd_test.sq3'
# connexion to DB
conn = sqlite3.connect(data_files)
# intermediaire temporary buffer between DB and connexion interface
cur = conn.cursor()

cur.execute(
    "insert into members(age, name, height) values(1,'Skarto', 1.2)")

# request for creating members table in DB
cur.execute("select * from members")

    # "insert into members(age, name, height) values('33', 'Fatima-Zahra', '1.69')")

# for line in cur:
#     print(line)

persons = cur.fetchall()
print(persons)


cur.close()
conn.close()
