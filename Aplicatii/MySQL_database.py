#!/usr/bin/python3

import MySQLdb

### Part 0 ### Connecting to DB

db = MySQLdb.connect('localhost', 'dj', 'root', 'python')

if db == None:
    print("Error connecting to the database")
else:
    print("All good")

cursor = db.cursor()

cursor.execute("SELECT VERSION();")
data = cursor.fetchall()
print(data)

### Part 1 ### Creating a Table and check it
try:
    cursor.execute("DROP TABLE IF EXISTS HOP")
    cursor.execute("""CREATE TABLE HOP (
                    NUME CHAR(20) NOT NULL,
                    VARSTA INT,
                    GENDER CHAR(1),
                    INTEREST CHAR(20));
                """)
    db.commit()
    print("TABLE CREATED")
except Exception:
    print("Operation failed")
    db.rollback()

### Part 2 ### Adding data to the table

sql = """INSERT INTO HOP (NUME, VARSTA, GENDER, INTEREST) VALUES ("Dominiq", 28, "M", "Python")"""

try:
    cursor.execute(sql)
    db.commit()
except Exception:
    print("Can't add to the dabase#2")
    db.rollback()

### Part 3 ### Adding data to the table via scripting

sql_query = (("Dominiq2", 29, "M", "Programare"), ("Adi", 28, "M", "Retele"), ("Gloria", 34, "F", "Apple"))

for user in sql_query:
    try:
        cursor.execute('INSERT INTO HOP (NUME, VARSTA, GENDER, INTEREST) VALUES ("%s", "%d", "%s", "%s")' %(user[0], user[1], user[2], user[3]))
        db.commit()
    except Exception:
        print("Operation not working...")
        db.rollback()

cursor.execute("SELECT * FROM HOP;")
data = cursor.fetchall()
print(data)

db.close()