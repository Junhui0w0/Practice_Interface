import tkinter as tk
from tkinter import *
import sqlite3

def func_register(id, pw):
    conn = sqlite3.connect('DB_Login.db')
    cursor = conn.cursor()
    cursor.execute(f'''
    insert into userinfo(userid, password) values('{id}', '{pw}');
''')
    
    conn.commit()
    
    return print('회원가입 완료')

root = tk.Tk()
root.title('register')
root.geometry('500x500')

id_lbl = tk.Label(root, text='User ID', background='yellow')
id_lbl.pack()

id_entry = tk.Entry(root)
id_entry.pack()

pw_lbl = tk.Label(root, text='Password', background='yellow')
pw_lbl.pack()

pw_entry = tk.Entry(root)
pw_entry.pack()

submit_btn = tk.Button(root, text='회원가입', command=lambda: func_register(id_entry.get(), pw_entry.get()))
submit_btn.pack()

root.mainloop()