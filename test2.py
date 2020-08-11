import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont



class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window = self
        self.background()
        self.leftcol()
        
        
        
    def background(self):
        self.window.geometry("1920x1080")
        self.window.title("Database")
        self.window["bg"] = "#222222"        
    
    def leftcol(self):
        ft1=tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
        # LBox=tk.Listbox(self.window,font =('device',"20"))
        # LBox.place(relheight=1,relwidth=0.1)

        # button=["Raw Data","Data Base","Report"]
        # for i in button:
        #     LBox.insert("end",i)
        L_canvas = tk.Canvas(self.window,bg="#424242",highlightthickness=0)
        L_canvas.place(relheight = 1,relwidth=0.15)

        B_rawdata = tk.Button(L_canvas,text="RawData")
        B_rawdata.place(relwidth=1,relheight=0.2)

        B_database=tk.Button(L_canvas,text = "DataBase")
        B_database.place(rely=0.2,relwidth=1,relheight=0.2)

        B_update = tk.Button(L_canvas,text="Update Data",font=ft1)
        B_update.place(rely=0.4,relwidth=1,relheight=0.2)






















Gui().mainloop()