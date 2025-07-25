import sqlite3 #작은 규모의 플젝 & 모바일 앱에서 주로 사용 (파일 기반)

conn = sqlite3.connect('test_on_tkinter.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO T1 (id, pw, text_data) values ('test1', '1234', 'hello world')")
conn.commit() #DB 변경사항 저장 커맨드
    #1. 기본적인 사용법 - SQL: https://miki3079.tistory.com/70
    #2. DB 내용 저장: https://coding-factory.tistory.com/997

cursor.execute('SELECT id, text_data from T1 where id = "test1"')

# data = cursor.fetchall()
# show_label.config(text=data)

# value = ''
# for v in data:
#     value = v

# print(v[1])