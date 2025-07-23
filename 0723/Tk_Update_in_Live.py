import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("UPDATE VALUE IN LVIE")
root.geometry("500x500")

def update_value(sv, label_name):
    label_name.config(text=sv.get()) 
        #https://stackoverflow.com/questions/24768455/tkinter-intvar-returning-py-var0-instead-of-value
            #1. sv(StringVar) 자체는 Tkinter의 object이기에 get() 메소드를 사용하지 않을 경우 PY_VAR0 출력

value_label = tk.Label(root, name='v_label', text='', background='yellow')
value_label.pack()

sv = StringVar() #Tkinter 내장 데이터타입
sv.trace("w", callback=lambda name, index, mode, sv=sv: update_value(sv, value_label))
    #https://stackoverflow.com/questions/6548837/how-do-i-get-an-event-callback-when-a-tkinter-entry-widget-is-modified

value_entry = tk.Entry(root, name='v_entry', textvariable=sv)
value_entry.pack()
root.mainloop()