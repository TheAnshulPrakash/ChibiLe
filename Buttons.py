from tkinter import *
import tkinter as tk

from tkinter import ttk
class ButtonFrame():

    
    def clickable_buttons(frame):
        
        BG_button='#f0e8d7'
        FG_button='#d5ff82'
        BG='#fcd7e1'
        FG='#660000'
        def button0_clicked():
            if button0.cget("text") == "Bulb Off":
                button0.config(text="Bulb On",bg=FG_button)
                
            else:
                button0.config(text="Bulb Off",bg=BG_button)
        def button1_clicked():
            if button1.cget("text") == "Study Lamp Off":
                button1.config(text="Study Lamp On",bg=FG_button)
            else:
                button1.config(text="Study Lamp Off",bg=BG_button)
        
        def button2_clicked():
            if button2.cget("text") == "Fan Off":
                button2.config(text="Fan On",bg=FG_button)
            else:
                button2.config(text="Fan Off",bg=BG_button)
        
        def button3_clicked():
            if button3.cget("text") == "Bedroom Lights Off":
                button3.config(text="Bedroom Lights On",bg=FG_button)
            else:
                button3.config(text="Bedroom Lights Off",bg=BG_button)
        
        def button4_clicked():
            if button4.cget("text") == "Drawing Lights Off":
                button4.config(text="Drawing Lights On",bg=FG_button)
            else:
                button4.config(text="Drawing Lights Off",bg=BG_button)


            
        button0 = tk.Button(frame, text="Bulb Off",width=15,height=1, bg=BG_button, fg=FG, command=button0_clicked)
        button1 = tk.Button(frame, text="Study Lamp Off", width=15,height=1,bg=BG_button, fg=FG, command=button1_clicked)
        button2 = tk.Button(frame, text="Fan Off", bg=BG_button,width=15,height=1, fg=FG, command=button2_clicked)
        button3 = tk.Button(frame, text="Bedroom Lights Off", bg=BG_button,width=15,height=1, fg=FG, command=button3_clicked)
        button4 = tk.Button(frame, text="Drawing Lights Off", bg=BG_button,width=15,height=1, fg=FG, command=button4_clicked)
        
        
        button0.grid(row=1, column=0, pady=10)
        button1.grid(row=2,column=0,pady=10)

        button2.grid(row=3, column=0,padx=10,pady=10)
        button3.grid(row=1, column=1, padx=10,pady=10)
        button4.grid(row=2, column=1, padx=10,pady=10)

    def slider(frame):
        var=IntVar()
        style=ttk.Style()
       
        style.configure("Custom.Vertical.TScale",background="#cfdcec")
        
        tempscale=ttk.Scale(frame,from_=100,to=-5,variable=var,orient="vertical",style="Custom.Vertical.TScale")
        #TempLabel=tk.Label(frame,text=var).grid(row=4,column=1)
       
        tempscale.grid(row=4,column=0,pady=10)
        

        

    
        
