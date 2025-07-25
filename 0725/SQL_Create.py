import sqlite3 #작은 규모의 플젝 & 모바일 앱에서 주로 사용 (파일 기반)

#1. DB 생성
conn = sqlite3.connect('test_on_tkinter.db')
cursor = conn.cursor()
cursor.execute('''
    create table T1
               (id VARCHAR(50) Primary key not null,
               pw varchar(50) not null,
               text_data varchar(1000)
               );
''')
