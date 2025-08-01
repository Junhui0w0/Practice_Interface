from tkinter import *
import tkinter as tk
import pymongo

import MongoDB
import get_typing_text

def create_child_window(parent_window, userID, userPW):
    res = MongoDB.get_userinfo(userID, userPW)

    if res != 'Success': #로그인 실패
        return 'Error: login_fail'

    def compare_answer(event, answer, user_text, score):
        global cnt, content

        score += 1

        print(answer)
        print(user_text)

        if answer == user_text:
            cnt += 1

            MongoDB.modify_score(userID)
            user_total_corret_lbl.config(text=f'현재까지의 {userID}님의 전체 정답 갯수: {score}', bg='yellow')

            print('정답')

        else:
            cnt = 0
            print('오답')

        streak_cnt_lbl.config(text=f'연속 정답 갯수: {cnt}')

        length = len(user_text)
        typing_entry.delete(0,length)
            # delete - https://lcs1245.tistory.com/entry/Python-tkinter-Entry-%EB%A7%8C%EB%93%A4%EA%B8%B0

        content = get_typing_text.get_text()
        typing_lbl.config(text=content)
            
    userScore = MongoDB.get_score(userID)

    child_window = tk.Toplevel(parent_window)
    child_window.wm_title('자식 윈도우 - Typing')
    child_window.geometry('1500x1500')

    name_lbl = tk.Label(child_window, text='Typing 연습', bg='yellow', font=('맑은고딕', 10))
    name_lbl.pack()

    user_total_corret_lbl = tk.Label(child_window,font=('맑은고딕', 10), text=f'현재까지의 {userID}님의 전체 정답 갯수: {userScore}', bg='yellow')
    user_total_corret_lbl.pack()

    streak_cnt_lbl = tk.Label(child_window, text=f'연속 정답 갯수: 0', font=('맑은고딕', 10))
    streak_cnt_lbl.pack()

    typing_lbl = tk.Label(child_window, text=content, font=('맑은고딕', 15), bg='black', fg='white')
    typing_lbl.pack()

    typing_entry = tk.Entry(child_window, font=('맑은고딕', 12), width=70)
    typing_entry.pack()

    child_window.bind('<Return>', lambda event: compare_answer(event, answer=content.rstrip().lstrip(), user_text=typing_entry.get(), score=userScore))
        # 바인드 - https://pylife.tistory.com/entry/tkinter-button-command-bind
        # 바인드 argument 사용 - https://stackoverflow.com/questions/72717440/binding-a-function-with-input-argument-to-a-tkinter-widget

cnt = 0
content = get_typing_text.get_text()

root = tk.Tk()
root.title('login and typing')
root.geometry('500x500')

id_lbl = tk.Label(root, text='아이디', bg='yellow')
id_lbl.pack()

id_entry = tk.Entry(root)
id_entry.pack()

pw_lbl = tk.Label(root, text='pw', bg='yellow')
pw_lbl.pack()

pw_entry = tk.Entry(root)
pw_entry.pack()

login_btn = tk.Button(root, text='로그인', command=lambda: create_child_window(root, id_entry.get(), pw_entry.get()))
login_btn.pack()

root.mainloop()