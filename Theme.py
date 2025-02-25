import tkinter as tk
from tkinter import ttk
from Icon import HomuChan_icon
from Display import DialogBox
import os
from SerialComm import SerialCommunication
class DropdownMenu():
    def theme_select(self, parent,window,Serial_frame,frame_anime,display_frame,Button_frame):
        options=[
            "Theme 1","Theme 2"
            ]
        
        HomuChan_icon.anime_photo(frame_anime,"C:/Users/rishi/PythonInterface/ControlPy/src/HomuChan1.png")
        self.var = tk.StringVar(value=options[0])
        self.prev_value = self.var.get()  # Store the initial value
        
        ttk.Label(parent, text="Select an option:", font=("Arial", 12))
        dropdown = ttk.Combobox(parent, textvariable=self.var, values=options, state="readonly", font=("Arial", 11), width=8)
        dropdown.grid(row=0,column=5)
        label = ttk.Label(parent, text=f"Selected: {self.var.get()}", font=("Arial", 12, "bold"))

        dropdown.bind("<<ComboboxSelected>>", lambda e: self.on_selection_change(label,parent,window,Serial_frame,frame_anime,display_frame,Button_frame))
        
    def on_selection_change(self,label,frame,window,Serial_frame,frame_anime,display_frame,Button_frame):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        
        new_value = self.var.get()
        BG2='#08063e'
        FG2='#ffffff'
        BG='#fcd7e1'
        FG='#660000'
        if new_value != self.prev_value:
            if new_value =="Theme 2": 
                image_name = "Anime_Photo_boy.png"
                image_path = os.path.join(script_dir, image_name)
                HomuChan_icon.anime_photo(frame_anime,image_path)
                print("Selected:", new_value)
                window.config(bg=BG2)
                frame.config(bg=BG2)
                Serial_frame.config(bg='#ecf0f1')

                
                display_frame.config(bg='#ecf0f1',)
                frame_anime.config(bg=BG2)
                Button_frame.config(bg=BG2)
            if new_value =="Theme 1":
                image_name = "OIG.png"
                image_path = os.path.join(script_dir, image_name)
                HomuChan_icon.anime_photo(frame_anime,image_path)
                print("Selected:", new_value)
                window.config(bg=BG)
                frame.config(bg=BG)
                Serial_frame.config(bg=BG)
                display_frame.config(bg='#ecf0f1',)
                frame_anime.config(bg=BG)
                Button_frame.config(bg=BG)
            
        
        self.prev_value = new_value  
        label.config(text=f"Selected: {new_value}")

    
    def port_select(self,frame,ports):
        clicked = tk.StringVar()
        def options(self): 
            print(clicked.get())
            DialogBox().text_serial("Now Connecting...")
            self.serial_comm = SerialCommunication(port=clicked.get(), baudrate=115200)
            self.serial_comm.connect()
            """"try:
                while True:
                    message = input("Enter message (or 'exit' to quit): ")
                    if message.lower() == "exit":
                        break
                    self.serial_comm.send_message(message)
            finally:
                self.serial_comm.disconnect()"""

            

        
        clicked.set("SELECT ONE")
        drop = ttk.Combobox(frame, textvariable=clicked, values=ports, state="readonly")
        drop.grid(row=1, column=0)
        drop.bind("<<ComboboxSelected>>", options)  
        
 