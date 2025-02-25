import tkinter as tk
from Data_sharing import comm_port_send
class DialogBox:
    def output_box(self, parent):
        global box
        box = tk.Text(parent, width=41, height=7, bg='#cfdcec', font=("Times New Roman", 10))
        box.grid(row=2, column=0)
        box.config(state="disabled")

    def text_whisper(self,string):
        box.config(state="normal")
        box.insert("end",string)
        box.config(state="disabled")
        
        
        
    def Serial_Box(self,parent):
        global Ser_Out
        tk.Label(parent,text="Serial Monitor",bg="#cfdcec").grid(row=3,column=0,columnspan=4)
        Ser_Out=tk.Text(parent, width=41, height=7, bg='#cfdcec', font=("Times", 10))
        
        Ser_Out.grid(row=4,column=0,columnspan=4,pady=1)
    
    
    def Serial_enter(self,parent):
        tk.Label(parent, text="Send Command:").grid(row=2, column=0,sticky="w",pady=5)
    
        entry = tk.Entry(parent, width=17)  
        entry.grid(row=2, column=1,sticky="w",pady=5)  
        parent.grid_rowconfigure(0,weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        def send(event):
            user_input = entry.get()
            print("User Input:", user_input)
            comm_port_send.put(user_input)
            entry.delete(0, tk.END)

        entry.bind("<Return>", send)



    def text_serial(self,string):
        Ser_Out.config(state="normal")
        Ser_Out.insert("end",string)
        Ser_Out.config(state="disabled")

    def clear_text_1(self):
        Ser_Out.config(state="normal")
        Ser_Out.delete("1.0", tk.END)
        Ser_Out.config(state="disabled")
        

    def get_text(self):
        return box.get(0, tk.END).strip()

    def clear_text(self):
        box.config(state="normal")
        box.delete("1.0", tk.END)
        box.config(state="disabled")

