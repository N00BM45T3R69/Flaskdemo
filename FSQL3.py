import sqlite3

con=sqlite3.connect("employee.db")
if con==True:
    print('Connected to Database')
con.execute('create table employees(id integer primary key autoincrement,name text not null,email text not null,address text not null)')
print('Created Table')
