import tkinter as tk

from PIL import Image,ImageTk
import ctypes

class HomuChan_icon():

    def __init__(self,parent):
        app_id = "Chibi Le.HomuChan"  
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        self.icon=Image.open("C:/Users/rishi/PythonInterface/ControlPy/src/Anime_Logo.png")
        self.icon=ImageTk.PhotoImage(self.icon)
        parent.iconphoto(True,self.icon)
    def anime_photo(parent,photo_address):
        img = Image.open(photo_address)
        img = img.resize((250, 250)) 
        global photo1 
        photo1 = ImageTk.PhotoImage(img)

        label1 = tk.Label(parent, image=photo1)
        label1.grid(row=4, column=0, columnspan=10)

