import tkinter as tk
from tkinter import *
import sqlite3 #모바일 앱 & 간단한 소규모 프로젝트에 적합

#DB connect
conn = sqlite3.connect('test_on_tkinter.db')
cursor = conn.cursor()

def get_text_data(id):
    a = cursor.execute(f'SELECT id, text_data from T1 where id = "{id}"')
    
    data = cursor.fetchall()
    if len(data) == 0:
        print('해당 데이터 존재X')
        return True
    
    for value in data:
        print('횟수+')
        show_label.config(text=f'ID: {value[0]} \nData: {value[1]}')

root = tk.Tk()
root.geometry('500x500')
root.title('SQLITE IN TKINTER')

id_label = tk.Label(root, name='id_lbl', text='아이디 검색', background='yellow')
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

search_btn = tk.Button(root, name='s_btn', text='조회', command = lambda: get_text_data(id_entry.get()))
search_btn.pack()

show_label = tk.Label(root, text='<작성된 내용>')
show_label.pack()

root.mainloop()