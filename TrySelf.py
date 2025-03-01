import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports
from Theme import DropdownMenu
from Display import DialogBox
from Buttons import ButtonFrame
from Icon import HomuChan_icon
from WhisperAI import WhisperTTS
import time

import threading

from Data_sharing import whisper_data

ports = [port.device for port in serial.tools.list_ports.comports()]
dropdown=DropdownMenu()





BG='#fcd7e1'
FG='#660000'

window = tk.Tk()
window.title("ChibiLe")

window.geometry('800x400')

window.resizable(False,False)
window.configure(background=BG)

HomuChan_icon(window)

frame = tk.Frame(bg=BG)
frame.place(x=260,y=0)


frame_anime = tk.Frame(bg=BG)
frame_anime.place(x=0,y=0)



frame_theme=tk.Frame(bg=BG)
frame_theme.place(x=615,y=0)



display_frame=tk.Frame(bg=BG)
display_frame.place(x=2,y=260)



Serial_frame=tk.Frame(bg=BG)
Serial_frame.place(x=545,y=200)

def update_Serial():
    dropdown.port_select(Serial_frame,ports)



t3=threading.Thread(target=update_Serial,daemon=True)
t3.start()



dropdown.theme_select(frame_theme,window,Serial_frame,frame_anime,display_frame,frame)

DialogBox().output_box(display_frame)
DialogBox().Serial_Box(Serial_frame)

DialogBox().Serial_enter(Serial_frame)

def WhisperThread():
    TTS=WhisperTTS()
    TTS.listen_and_transcribe(Whisper_On)

def updateDialog():
    while Whisper_On:
        value=whisper_data.get()
        if value=="Listening\n": DialogBox().clear_text()

        print(f"Output {value}")
        DialogBox().text_whisper(value)
        time.sleep(0.8)



def to_start_whisper():
    global Whisper_On,t1,t2
    if var.get():
        Whisper_On=True
        
        t2=threading.Thread(target=updateDialog,daemon=True)
        t1 = threading.Thread(target=WhisperThread, daemon=True)
        t1.start()    
        t2.start()


    else :
        Whisper_On=False
        DialogBox().clear_text()


var = tk.IntVar()



if_whisper=tk.Checkbutton(display_frame, text="Use Speech Commands", variable=var,command=to_start_whisper,bg='#ffffff',height=1)
if_whisper.grid(row=0,column=0)





ButtonFrame.clickable_buttons(frame)
ButtonFrame.slider(frame)





window.mainloop()

