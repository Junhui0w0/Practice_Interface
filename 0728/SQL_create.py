import sqlite3

conn = sqlite3.connect('DB_Login.db')
cursor = conn.cursor()
cursor.execute('''
    create table userinfo(
               userid varchar(50) primary key not null,
               password varchar(50) not null
               );
''')