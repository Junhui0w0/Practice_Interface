from tkinter import *
import tkinter as tk
import sqlite3

def func_login(id, pw):
    conn = sqlite3.connect('DB_Login.db')
    cursor = conn.cursor()
    
    cursor.execute(f'''
        select * from userinfo where userid = '{id}' and password = '{pw}';
''')
    
    tmp = cursor.fetchall()
    
    for data in tmp:
        print(data)

    if len(tmp) == 0:
        return print('로그인 실패')
    
    else:
        return print('로그인 성공')

root = tk.Tk()
root.title('login')
root.geometry('500x500')

id_lbl = tk.Label(root, text='User ID', background='yellow')
id_lbl.pack()

id_entry = tk.Entry(root)
id_entry.pack()

pw_lbl = tk.Label(root, text='Password', background='yellow')
pw_lbl.pack()

pw_entry = tk.Entry(root)
pw_entry.pack()

submit_btn = tk.Button(root, text='로그인', command=lambda: func_login(id_entry.get(), pw_entry.get()))
submit_btn.pack()

root.mainloop()