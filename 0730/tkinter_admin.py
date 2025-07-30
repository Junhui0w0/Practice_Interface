from tkinter import *
import tkinter as tk
from MongoDB import submit_userinfo

root = tk.Tk()
root.title('mongoDB-MCTX-Admin [Ver:0.0.1]')
root.geometry("500x500")

id_label = tk.Label(root, text='아이디', background='yellow')
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

pw_label = tk.Label(root, text='패스워드', background='yellow')
pw_label.pack()

pw_entry = tk.Entry(root)
pw_entry.pack()

submit_btn = tk.Button(root, text='회원가입', command= lambda: submit_userinfo(id_entry.get(), pw_entry.get()))
submit_btn.pack()

root.mainloop()