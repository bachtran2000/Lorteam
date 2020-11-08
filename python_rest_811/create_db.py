
import sqlite3


sqliteConnection = sqlite3.connect('Xanh.db')
print("Successfully Connected to SQLite")
cursor = sqliteConnection.cursor()
sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()
print("SQLite table created")
cursor.close()



if (sqliteConnection):
    sqliteConnection.close()
    print("sqlite connection is closed")