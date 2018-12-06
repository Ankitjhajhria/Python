#this for exampling with sql

#we will import sql now
import sqlite3

#we will now connect py with sql

conn = sqlite3.connect('employees.db')

c = conn.cursor()

#now we will create a data base
c.execute("CREATE DATABASE employees.db")
c.execute("USE emoloyees.db")
