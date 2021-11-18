import sqlite3

path = '/home/ehp/Documents/Python-codes/TeacherDuNet/gerard_swinnen_python/bdd/dogs_bd.sq3'



with sqlite3.connect(path) as conn:
    cur = conn.cursor()
    try:
        cur.execute("SELECT datetime('now', 'localtime')")
        print(cur.fetchone()[0])
        cur.execute('UPDATE dogs SET dog_name = ? WHERE dog_name = ?', ('Skarito', 'skarto'))
        # cur.execute('DELETE FROM dogs WHERE dog_name="boscou"')
        cur.execute('SELECT * FROM dogs')
        dogs = cur.fetchall()
        print(dogs)
    except sqlite3.OperationalError as e:
        print(e)

