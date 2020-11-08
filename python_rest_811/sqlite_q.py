import sqlite3

conn = sqlite3.connect('Xanh.db')

c = conn.cursor()
c.execute('SELECT * FROM tripdata')
print (c.fetchall())
# c.execute('SELECT * FROM ')
# print (c.fetchall())
conn.close()