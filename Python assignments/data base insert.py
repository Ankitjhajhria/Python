

#this for creating and instertin  with sqlite3

#we will import sql now
import sqlite3

#we will now connect py with sql

conn = sqlite3.connect('employees.db')

c = conn.cursor()

#now we will make a new table

"""c.execute(""create table PO
            (id INGTEGER,
            first TEXT,
            last TEXT,
            pay INTEGER)"")"""

#we will do in for loop
id = 01
first = "'BSDU'"
last = "'university'"
pay = 500000
c.execute("""INSERT INTO PO
            VALUES ({}, {}, {}, {})"""
          .format(id, first, last, pay))




c.execute("""select * from PO""")

print c.fetchall()
