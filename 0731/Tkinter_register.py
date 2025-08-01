import tkinter as tk
from tkinter import *
import MongoDB

def submit_userinfo(id, pw):
    MongoDB.submit_userinfo(id, pw)

root = tk.Tk()
root.title('register form')
root.geometry('500x500')

id_lbl = tk.Label(root, text='아이디', bg='yellow')
id_lbl.pack()

id_entry = tk.Entry(root)
id_entry.pack()

pw_lbl = tk.Label(root, text='비번', bg='yellow')
pw_lbl.pack()

pw_entry = tk.Entry(root)
pw_entry.pack()

submit_btn = tk.Button(root, text='회원가입', command=lambda: submit_userinfo(id_entry.get(), pw_entry.get()))
submit_btn.pack()

root.mainloop()