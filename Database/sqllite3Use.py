import sqlite3


# sql connect
# conn = sqlite3.connect('./Database/test_sqlite.db')
conn = sqlite3.connect(':memory:')

# make curs
curs = conn.cursor()

# make talble
curs.execute(
     'CREATE TABLE person(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

# commit db
# conn.commit()

# insert data
curs.execute(
    'INSERT INTO person(name) VALUES("leeyonghoon")')
curs.execute(
    'INSERT INTO person(name) VALUES("kimyoungsun")')
curs.execute(
    'INSERT INTO person(name) VALUES("leekyongrae")')
curs.execute(
    'INSERT INTO person(name) VALUES("leehojinjinjara")')
conn.commit()
# See data in console
curs.execute('SELECT * from person')
print(curs.fetchall())

# Upate data  where**
curs.execute('UPDATE person set name="ganziyonghoon" where name="leeyonghoon"')

# See data in console
curs.execute('SELECT * from person')
print(curs.fetchall())

# Delete data whrer**
curs.execute('DELETE from person where name = "ganziyonghoon"')

# See data in console
curs.execute('SELECT * from person')
print(curs.fetchall())


conn.commit()
# connect close
conn.close()
