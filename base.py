from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *
import tkinter as tk
import pytube
import os
import re
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#pyinstaller -w -i="asf.ico" --add-data '.\icon.png;.' -F base.py

#변수 이름은 "홍윤석"씨가 추천해줌 내 의지 아님 ;;
bybabo = Tk() # 변수 정의 
bybabo.title("BB Downloader") # 창 이름 정의
bybabo.geometry("240x100") # 창 해상도 정의 
bybabo.resizable(False, False)  # 창 해상도 변경 금지 
#bybabo.iconphoto(False, tk.PhotoImage(file=resource_path("./icon.png"))) # 아이콘 정의
def onclick(): # 버튼을 클릭했을때 
    bt["text"] = "잠시만 기다려요.." # 버튼 이름 바꾸기 
    try:
        bt["text"] = "잠시만 기다려요.." # 버튼 이름 바꾸기 
        pytube.YouTube(tk.Entry.get(input)).streams.filter(only_audio=True).first().download('./BB Download Temp') # 오디오 받기 
        uwu = YouTube(tk.Entry.get(input)).title # 받은 오디오의 확장자를 변환하기 위해 제목을 가져옴 
        uwu = re.sub("[/'*?><|]","", uwu) # 제목 필터링 
        os.rename(f'.\BB Download Temp\{uwu}.mp4',f'.\BB Download Temp\{uwu}.mp3') # 받은 mp4 파일을 mp3로 변환
        pytube.YouTube(tk.Entry.get(input)).streams.filter(res="1080p").first().download('./BB Download Temp') # 영상 다운로드 
        videoclip = VideoFileClip(f'.\BB Download Temp\{uwu}.mp4') # 다운받은 mp4 파일을 영상 대기열에 추가 
        audioclip = AudioFileClip(f'.\BB Download Temp\{uwu}.mp3') # 다운받은 mp3 파일을 오디오 대기열에 추가
        videoclip.audio = audioclip # 영상 대기열과 오디오 대기열을 연결 
        videoclip.write_videofile(f'.\YouTubeDownload\{uwu}.mp4') # 대기열에 있는 영상 파일을 인코딩함
        videoclip.close() # 메모리에 있는 영상 데이터 초기화
        audioclip.close() # 메모리에 있는 오디오 데이터 초기화
        messagebox.showinfo("좋아요!", """다운로드에 성공했어요! 파일은 "./BB Download" 에 넣어둘께요!""") # 창 띄우기 
        bt["text"] = "슈우웅!"
    except pytube.exceptions.RegexMatchError: # pytube 오류 처리
        bt["text"] = "이런!"
        messagebox.showinfo("이런!", """다운로드에 실패했어요..... url을 다시 확인해주세요.....""")
        bt["text"] = "슈우웅!"
    except FileExistsError: # 파일 충돌 처리 내일 자동화 할 예정 
        bt["text"] = "이런!"
        messagebox.showinfo("이런!", """파일 충돌이 발생했어요 ./BB Downloader Temp 폴더를 지워주세요...""")
        bt["text"] = "슈우웅!"
    except: # 이외 오류 처리
        bt["text"] = "이런!"
        messagebox.showinfo("이런!", """알 수 없는 오류가 발생했어요...""")
        bt["text"] = "슈우웅!"
text = Label(bybabo, text="url을 입력해주세요!") # 텍스트 속성 값
input = Entry(bybabo) 
bt = Button(bybabo, text="슈우웅!", command=onclick)
text.pack()
input.pack()
bt.pack()
bybabo.mainloop()