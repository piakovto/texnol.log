import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

from istoriko import *
from portof import *
from kataxor import *
from welcome_screen import *

class App:
    def __init__(self, root):
        
        #setting title
        root.title("Cheapstr")
        #setting window size
        width=1250
        height=750
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Fwelcome = Frame(root, width=950, height=625, highlightbackground="black", highlightthickness=1)
        Fwelcome.grid(row=0,column=0,sticky="nsew")
        Fwelcome.pack(fill=None, side='right', expand='False')
        Fwelcome.place(x=250,y=100)

        
        Fportof = Frame(root, width=950, height=625, highlightbackground="black", highlightthickness=1)
        Fportof.grid(row=0,column=0,sticky="nsew")
        Fportof.pack(fill=None, side='right', expand='False')
        Fportof.place(x=250,y=100)

        Fdapanh = Frame(root, width=950, height=625, highlightbackground="black", highlightthickness=1)
        Fdapanh.grid(row=0,column=0,sticky="nsew")
        Fdapanh.pack(fill=None, side='right', expand='False')
        Fdapanh.place(x=250,y=100)
     
        Fistoriko = Frame(root, width=950, height=625, highlightbackground="black", highlightthickness=1)
        Fistoriko.grid(row=0,column=0,sticky="nsew")
        Fistoriko.pack(fill=None, side='right', expand='False')
        Fistoriko.place(x=250,y=100)



        welcome(Fwelcome)
        Gui_istoriko(Fistoriko)
        Gui_portof(Fportof)


        Fwelcome.tkraise()

        
        Dapanh_but=tk.Button(root)
        Dapanh_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Dapanh_but["font"] = ft
        Dapanh_but["fg"] = "#000000"
        Dapanh_but["justify"] = "center"
        Dapanh_but["text"] = "Νέα Δαπάνη"
        Dapanh_but.place(x=30,y=110,width=200,height=35)
        Dapanh_but["command"] = Fdapanh.tkraise

        Apotam_but=tk.Button(root)
        Apotam_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Apotam_but["font"] = ft
        Apotam_but["fg"] = "#000000"
        Apotam_but["justify"] = "center"
        Apotam_but["text"] = "Αποταμίευση"
        Apotam_but.place(x=30,y=170,width=200,height=35)
        Apotam_but["command"] = self.Statist_but_command

        Istoriko_but=tk.Button(root)
        Istoriko_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Istoriko_but["font"] = ft
        Istoriko_but["fg"] = "#000000"
        Istoriko_but["justify"] = "center"
        Istoriko_but["text"] = "Ιστορικό Δαπανών"
        Istoriko_but.place(x=30,y=240,width=200,height=35)
        Istoriko_but["command"] = Fistoriko.tkraise
        
        Statist_but=tk.Button(root)
        Statist_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Statist_but["font"] = ft
        Statist_but["fg"] = "#000000"
        Statist_but["justify"] = "center"
        Statist_but["text"] = "Στατιστικά δαπανών"
        Statist_but.place(x=30,y=310,width=200,height=35)
        Statist_but["command"] = self.Statist_but_command

        Settings_but=tk.Button(root)
        Settings_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Settings_but["font"] = ft
        Settings_but["fg"] = "#000000"
        Settings_but["justify"] = "center"
        Settings_but["text"] = "Ρυθμίσεις Εφαρμογής"
        Settings_but.place(x=30,y=640,width=200,height=35)
        Settings_but["command"] = self.Settings_but_command

        Log_out_but=tk.Button(root)
        Log_out_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Log_out_but["font"] = ft
        Log_out_but["fg"] = "#000000"
        Log_out_but["justify"] = "center"
        Log_out_but["text"] = "Αποσύνδεση"
        Log_out_but.place(x=30,y=690,width=90,height=25)
        Log_out_but["command"] = self.Log_out_but_command

        Change_user_but=tk.Button(root)
        Change_user_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Change_user_but["font"] = ft
        Change_user_but["fg"] = "#000000"
        Change_user_but["justify"] = "center"
        Change_user_but["text"] = "Αλλαγή Χρήστη"
        Change_user_but.place(x=140,y=690,width=90,height=25)
        Change_user_but["command"] = self.Change_user_but_command

        GLabel_737=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["justify"] = "center"
        GLabel_737["text"] = "Διαθέσiμο υπόλοιπο:"
        GLabel_737.place(x=0,y=40,width=154,height=30)

        Plus_but=tk.Button(root)
        Plus_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=20)
        Plus_but["font"] = ft
        Plus_but["fg"] = "#000000"
        Plus_but["justify"] = "center"
        Plus_but["text"] = "+"
        Plus_but["relief"] = "ridge"
        Plus_but.place(x=200,y=40,width=25,height=25)
        Plus_but["command"] = Fportof.tkraise

        """
        lus_but=tk.Button(f1)
        lus_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=20)
        lus_but["font"] = ft
        lus_but["fg"] = "#000000"
        lus_but["justify"] = "center"
        lus_but["text"] = "+"
        lus_but["relief"] = "ridge"
        lus_but.place(x=250,y=40,width=25,height=25)
        

        
        dlus_but=tk.Button(f2)
        dlus_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=20)
        dlus_but["font"] = ft
        dlus_but["fg"] = "#000000"
        dlus_but["justify"] = "center"
        dlus_but["text"] = "+"
        dlus_but["relief"] = "ridge"
        dlus_but.place(x=20,y=40,width=25,height=25)
        """
    

    def Dapanh_but_command(self):
        f1.tkraise()


    def Apotam_but_command(self):
        f2.tkraise()


    def Istoriko_but_command(self):
        print("command")


    def Statist_but_command(self):
        print("command")


    def Settings_but_command(self):
        print("command")


    def Log_out_but_command(self):
        print("command")


    def Change_user_but_command(self):
        print("command")


    def Plus_but_command(self):
        print("command")




    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.update_idletasks()
    root.mainloop()
