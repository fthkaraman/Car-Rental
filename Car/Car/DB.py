import sqlite3

dbase = sqlite3.connect('Our_data.db')

dbase.execute(''' CREATE TABLE IF NOT EXISTS USERS(
USERNAME TEXT PRIMARY KEY NOT NULL,
PASSWORD TEXT NOT NULL) ''')

dbase.execute(''' INSERT INTO USERS VALUES(?,?)''',('Fatih','2244'))

dbase.commit()