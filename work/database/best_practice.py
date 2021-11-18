import sqlite3

path = '/home/ehp/Documents/Python-codes/TeacherDuNet/gerard_swinnen_python/bdd/dogs_bd.sq3'
data = []
print("how many dog names will be added to the db? ")
dogs_cnt = int(input())
for dog in range(dogs_cnt):
    print(f"enter the {dog+1}'t dog's info? ")
    age = int(input("age? "))
    name = input("name? ")
    height = float(input("height? "))
    data.append((age, name, height))


# data = [(1, 'skarto', 1), (8, 'boscou', 1.5), (13, 'box', 1.3)]

with sqlite3.connect(path) as conn:
    cur = conn.cursor()
    
    try:
        cur.executescript("""
            DROP TABLE IF EXISTS dogs;
            CREATE TABLE dogs(
                age INT, 
                dog_name TEXT, 
                height REAL
            );
        """)
    
        cur.executemany("INSERT INTO dogs(age,dog_name,height) VALUES(?, ?, ?)", data)
    except sqlite3.OperationalError as e:
        print(e)

# conn.commit()
# cur.close()
# conn.close()
