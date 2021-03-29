from tkinter import *
from tkinter import messagebox
import tkinter as tk

#변수 이름은 "홍윤석"씨가 추천해줌 내 의지 아님 ;;
bybabo = Tk()
bybabo.title("TEST")
bybabo.geometry("640x280")
bybabo.resizable(False, False) 

def onclick():
    bt["text"] = "잠시만 기다려요.."
    messagebox.showinfo("좋아요!", """다운로드에 성공했어요! 파일은 "./YoutubeDownload" 에 넣어둘께요!""")
    bt["text"] = "url을 입력해주세요!"

text = Label(bybabo, text="url을 입력해주세요!")
input = Entry(bybabo)
bt = Button(bybabo, text="슈우웅!", command=onclick)
text.pack()
input.pack()
bt.pack()
bybabo.mainloop()