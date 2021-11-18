import sqlite3
import psycopg2


path = "/home/ehp/Documents/Python-codes/TeacherDuNet/gerard_swinnen_python/bdd/music_db/music_db.db"
with sqlite3.connect(path) as conn:
    cur = conn.cursor()
    cur.executescript('SELECT * FROM compositors')
    comp = cur.fetchall()
    print(comp)

with sqlite3.connect(path) as conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM works')
    works = cur.fetchall()
    print(works)