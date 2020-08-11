import tkinter as tk
import tkinter.messagebox #弹窗
from tkinter import filedialog #编辑文件夹
import tkinter.font as tkFont #字体
import os
import shutil


class Gui():
    def __init__(self,window):
        
        self.window = window
        self.background()
        self.leftcol()
        self.downbar()

        self.raw_directory=""
        self.database=""
        self.getplace=""
        
        
        
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
        L_canvas = tk.Canvas(self.window,bg="#424242",highlightthickness=0,)
        L_canvas.place(relheight = 1,relwidth=0.15)

        B_rawdata = tk.Button(L_canvas,text="RawData",font=ft1,command=lambda: self.B_function("raw"))
        B_rawdata.place(relwidth=1,relheight=0.2)

        B_database=tk.Button(L_canvas,text = "DataBase",font=ft1,command = lambda:self.B_function("database"))
        B_database.place(rely=0.2,relwidth=1,relheight=0.2)

        B_update = tk.Button(L_canvas,text="Update Data",font=ft1,command = lambda: self.B_function("update"))
        B_update.place(rely=0.4,relwidth=1,relheight=0.2)

        B_quit = tk.Button(L_canvas,text="Quit",font=ft1,command = lambda: self.B_function("quit"))
        B_quit.place(rely=0.8,relwidth=1,relheight=0.2)

        
    def downbar(self):
        ft1=tkFont.Font(family='Fixdsys', size=18, weight=tkFont.BOLD)
        bar=tk.Canvas(self.window,bg="#424242",highlightthickness=0)
        bar.place(relheight=0.2,relwidth=0.85,rely=0.8,relx=0.15,)
        # bar.pack(fill="x",side="bottom",expand=True)

        label_input=tk.Label(bar,text="Place input:",font=ft1,bg="#424242",fg="white",)
        label_input.grid(row=0,column=0)
         # label_input.place(relx=0,rely=0.09)
        
        label_cs1=tk.Label(bar,text=" Current status: ",font=ft1,bg="#424242",fg="white",)
        label_cs1.grid(row=1,column=0,)
        # label_input.place(relx=-0.01,rely=0.3)

        label_cs2=tk.Label(bar,font=ft1,bg="#424242",fg="white",)
        label_cs2.grid(row=1,column=1,)
        # label_input.place(relx=-0.01,rely=0.3)

        placeinput = tk.Entry(bar,font=ft1,bg="#222222",fg="white")
        placeinput.grid(row=0,column=1)
        # placeinput.place(relx=0.115,rely=0.1)
        
        # B_reset = tk.Button(bar,text="Reset",font=ft1)
        # B_reset.grid(row=3,column=1)

        def getinfo(info):
            label_cs2["text"]=info
            self.getplace = info
           
        B_getplace = tk.Button(bar,text="Getplace",font=ft1,command=lambda: getinfo(placeinput.get()))
        B_getplace.grid(row=3,column=1)


        
        


    def B_function(self,functiontype,label=None):
        #leftcolumn
        if functiontype == ("raw"):
            self.raw_directory=filedialog.askdirectory()
        elif functiontype ==("database"):
            self.database=filedialog.askdirectory()
        elif  functiontype ==("quit"):
            window.destroy()
        elif functiontype ==("update"):
            if not len(self.raw_directory) == 0 and not len(self.database) == 0:
                database = self.database + r"/"+self.getplace
                decision=tk.messagebox.askokcancel("Warming",r"Raw data: {}".format(self.raw_directory)+ "\n\n"+r"Database: {}".format(database))
                if decision:
                    self.data_save(database)
            else:
                tkinter.messagebox.showinfo('Warming','please choose directory')
        
    def data_save(self,database):
        if os.path.exists(database):
            print("already exist")
        else:
            shutil.copytree(self.raw_directory,database)
    
        # downbar
        


















window = tk.Tk()
gui = Gui(window)
window.mainloop()