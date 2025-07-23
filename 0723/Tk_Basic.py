from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('20250723')
root.geometry('500x500')

cnt = 0

def click_button_increase_value(btn_name):
    global cnt

    cnt += 1
    btn_name.config(text=str(cnt))

def reset_button(btn_name):
    global cnt
    
    cnt = 0
    btn_name.config(text=str(cnt))


click_btn = tk.Button(root, name='show_value', text=str(cnt), command=lambda: click_button_increase_value(click_btn))
click_btn.pack()

reset_btn = tk.Button(root, name='reset_value', text='Reset Count', command=lambda: reset_button(click_btn))
reset_btn.pack()


root.mainloop()