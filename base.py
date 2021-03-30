from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pytube


#변수 이름은 "홍윤석"씨가 추천해줌 내 의지 아님 ;;
bybabo = Tk() # 변수 정의 
bybabo.title("BOYEON BABO") # 창 이름 정의
bybabo.geometry("240x100") # 창 해상도 정의 
bybabo.resizable(False, False)  # 창 해상도 변경 금지 
bybabo.iconphoto(False, tk.PhotoImage(file='./icon.png')) # 아이콘 정의
def onclick(): # 버튼을 클릭했을때 
    bt["text"] = "잠시만 기다려요.." # 버튼 이름 바꾸기 + 시발 이거 왜이레 
    try:
        pytube.YouTube(tk.Entry.get(input)).streams.get_highest_resolution().download('./YoutubeDownload') # Entrl 에 있는 값을 받은 후 유튜브 다운로드 
        messagebox.showinfo("좋아요!", """다운로드에 성공했어요! 파일은 "./YoutubeDownload" 에 넣어둘께요!""") # 창 띄우기
        bt["text"] = "222" 
    except:
        bt["text"] = "이런!"
        messagebox.showinfo("이런!", """다운로드에 실패했어요..... url을 다시 확인해주세요.....""")
        bt["text"] = "슈우웅!"

text = Label(bybabo, text="url을 입력해주세요!") # 텍스트 속성 값
input = Entry(bybabo) 
bt = Button(bybabo, text="슈우웅!", command=onclick)
text.pack()
input.pack()
bt.pack()
bybabo.mainloop()