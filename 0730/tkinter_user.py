import tkinter as tk
from tkinter import *
from MongoDB import get_userinfo

root = tk.Tk()
root.title('mongoDB-MCTX-User [Ver:0.0.1]')
root.geometry("500x500")

id_label = tk.Label(root, text='아이디', background='yellow')
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

pw_label = tk.Label(root, text='패스워드', background='yellow')
pw_label.pack()

pw_entry = tk.Entry(root)
pw_entry.pack()

submit_btn = tk.Button(root, text='로그인', command= lambda: get_userinfo(id_entry.get(), pw_entry.get()))
submit_btn.pack()

root.mainloop()