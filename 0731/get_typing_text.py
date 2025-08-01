import os
# os.chdir('0731\\타자연습_data')
typing_lst = os.listdir('0731\\타자연습_data\\.')
# print(typing_lst)
    # os 라이브러리 - https://speedspeed.tistory.com/172

import random
idx = random.randint(0, len(typing_lst)-1)
typing_file_name = typing_lst[idx]

def get_text():
    with open(f'0731\\타자연습_data\\{typing_file_name}', 'r', encoding='euc-kr') as f:
        # encoding='utf-8' -> 인코딩 에러 발생 -> euc-kr 변경 후 해결: https://blog.naver.com/jonghong0316/223929241660
        text = f.readlines()
        length = len(text)

        idx = random.randint(0, length-1)

        text[idx] = text[idx].replace('"', '')
        text[idx] = text[idx].replace("'", '')
        text[idx].rstrip()
        text[idx].lstrip()
        # text[idx] = text[idx].replace('"?', '')
        return text[idx]