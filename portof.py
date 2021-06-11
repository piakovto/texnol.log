import tkinter as tk
import tkinter.font as tkFont
import elegxos as el
import tkinter.ttk as tkk
import pickle
from oria import *


class Portof():
        def __init__(self, cash, card, categories, oria):
                self.cash = cash
                self.card = card
                self.categories = categories
                self.oria = oria
        def get_cash(self):
                return self.cash

        def set_cash(self, x):
                self.cash = x

        def get_card(self):
                return self.card

        def set_card(self, x):
                self.card = x

        def metakulish(self, poso, pros):
                elegxos = el.Elegxos("metakulish", poso, pros, "", self.cash, self.card)
                if (elegxos.create_diadikasia_elegxou() == 1):

                        if (pros == "Μετρητά"):
                                self.cash = int(self.cash) + int(poso)
                                self.card = int(self.card) - int(poso)
                        if (pros == "Κάρτα"):
                                self.cash = int(self.cash) - int(poso)
                                self.card = int(self.card) + int(poso) # 8elei apo8hkeush sto istoriko
                self.save_portof()
        def save_portof(self):
                fl = open("portof", "wb")
                pickle.dump(self, fl)
                fl.close()
        def save_istoriko(self, kataxorisi):
                fl = open("qwerty", "ab")
                pickle.dump(kataxorisi, fl)
                fl.close()
        
        def tess(self, katax):
                
                
                if (katax.katigoria == 1): #ta esoda exoun kategori to 1
                        if (katax.typos_plir == "Μετρητά"):
                                self.cash = int(self.cash) + int(katax.poso_katax)
                                result = 3
                        elif (katax.typos_plir == "Κάρτα"):
                                self.card = int(self.card) + int(katax.poso_katax)
                                result = 3

                else:
                         
                         for main, sub in categories.items():
                                 if (katax.katigoria in sub):
                                         katig = main

                         if (katig == "ΣΠΙΤΙ"):
                                orio_kathg = self.oria.spiti
                         elif (katig ==  "ΑΥΤΟΚΙΝΗΤΟ"):
                                orio_kathg = self.oria.car
                         elif (katig == "ΕΚΠΑΙΔΕΥΣΗ"):
                                orio_kathg = self.oria.educat
                         elif (katig == "ΙΑΤΡΙΚΑ"):
                                orio_kathg = self.oria.doctor
                         elif (katig == "ΔΙΑΣΚΕΔΑΣΗ"):
                                orio_kathg = self.oria.fun
                         elif (katig == "ΔΙΑΦΟΡΑ"):
                                orio_kathg = self.oria.etc

                         
                         if (katax.typos_plir == "Μετρητά"):
                                 ee = el.Elegxos(katax.typos, katax.poso_katax, katax.typos_plir, katig, orio_kathg, p.cash)
                                 result = ee.create_diadikasia_elegxou()
                         elif (katax.typos_plir == "Κάρτα"):
                                 ee = el.Elegxos(katax.typos, katax.poso_katax, katax.typos_plir, katig, orio_kathg, p.card)
                                 result = ee.create_diadikasia_elegxou()


                if (result == 0):
                        self.cash = self.cash - int(katax.poso_katax)
                        self.save_istoriko(katax)
                        self.save_portof()
                        return result
                else:
                        return result
        
                

categories = {
    "ΣΠΙΤΙ":
        ["Ενοίκιο",
        "Τηλέφωνο",
        "Ρεύμα",
         "Νερό",
         "Θέρμανη",
         "Κινητό",
         "Σούπερμάρκετ"],
     "ΑΥΤΟΚΙΝΗΤΟ":
        ["Καύσιμα",
          "Service",
          "Ασφάλεια",],
     "ΕΚΠΑΙΔΕΥΣΗ":
        ["Φροντιστήριο",
          "Βιβλία",
          "Δίδακτρα"],
    "ΙΑΤΡΙΚΑ":
        ["Επίσκεψη",
          "Φάρμακα"],
    "ΔΙΑΣΚΕΔΑΣΗ":
        ["Διασκέδαση"],
    "ΔΙΑΦΟΡΑ":
        ["Διάφορα"]
    }


p = Portof(0, 0, categories, orio)

fl = open("portof", 'rb')
p = pickle.load(fl)
fl.close()

def Metakul_but_command(x, poso_card_gui, poso_cash_gui):
                def GButton_796_command(po, pro):
                        p.metakulish(po, pro)
                        poso_cash_gui.config(text = p.cash)
                        poso_card_gui.config(text = p.card)

                Metakulish_Window = tk.Toplevel(x)

                Metakulish_Window.title("Μετακύλιση ποσού")

                Metakulish_Window.geometry("300x200")
                Metakulish_Window.resizable(width=False, height=False)

                GLabel_610=tk.Label(Metakulish_Window)
                ft = tkFont.Font(family='Times',size=10)
                GLabel_610["font"] = ft
                GLabel_610["fg"] = "#333333"
                GLabel_610["justify"] = "center"
                GLabel_610["text"] = "Ποσό:"
                GLabel_610.place(x=0,y=50,width=70,height=25)

                GLabel_256=tk.Label(Metakulish_Window)
                ft = tkFont.Font(family='Times',size=10)
                GLabel_256["font"] = ft
                GLabel_256["fg"] = "#333333"
                GLabel_256["justify"] = "center"
                GLabel_256["text"] = "Προς:"
                GLabel_256.place(x=0,y=130,width=70,height=25)

                GLineEdit_410=tk.Entry(Metakulish_Window)
                GLineEdit_410["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times',size=10)
                GLineEdit_410["font"] = ft
                GLineEdit_410["fg"] = "#333333"
                GLineEdit_410["justify"] = "center"
                GLineEdit_410["text"] = "Entry"
                GLineEdit_410.place(x=60,y=50,width=100,height=25)

                Select_box_metak=tkk.Combobox(Metakulish_Window, state="readonly")
                Select_box_metak['values'] = ('Μετρητά', 'Κάρτα')
                ft = tkFont.Font(family='Times',size=10)
                Select_box_metak["font"] = ft
                Select_box_metak["justify"] = "center"
                Select_box_metak.place(x=60,y=130,width=100,height=30)

                GButton_796=tk.Button(Metakulish_Window)
                GButton_796["bg"] = "#efefef"
                ft = tkFont.Font(family='Times',size=10)
                GButton_796["font"] = ft
                GButton_796["fg"] = "#000000"
                GButton_796["justify"] = "center"
                GButton_796["text"] = "Μετακύλιση"
                GButton_796.place(x=200,y=90,width=70,height=25)
                GButton_796["command"] = lambda: [GButton_796_command(GLineEdit_410.get(), Select_box_metak.get())]




def Gui_portof(x):


        def Prosth_but_command():
                x1 = Poso_entry.get()
                x2 = Select_box.get()
                if (x2 == "Μετρητά"):
                        p.set_cash(p.cash + int(x1))
                        Poso_metrhta.config(text = p.cash)
                elif (x2 == "Κάρτα"):
                        p.set_card(p.card + int(x1))
                        Poso_kartas.config(text = p.card)
                p.save_portof()
       
        GLabel_861=tk.Label(x)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "center"
        GLabel_861["text"] = "Πορτοφόλι"
        GLabel_861.place(x=30,y=10,width=181,height=40)

        GLabel_394=tk.Label(x)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_394["font"] = ft
        GLabel_394["fg"] = "#333333"
        GLabel_394["justify"] = "center"
        GLabel_394["text"] = "Μετρητά:"
        GLabel_394.place(x=40,y=70,width=87,height=30)

        GLabel_464=tk.Label(x)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Κάρτα:"
        GLabel_464.place(x=40,y=100,width=89,height=30)

        

        Poso_metrhta=tk.Label(x)
        ft = tkFont.Font(family='Times',size=10)
        Poso_metrhta["font"] = ft
        Poso_metrhta["fg"] = "#333333"
        Poso_metrhta["justify"] = "center"
        Poso_metrhta["text"] = p.cash
        Poso_metrhta.place(x=140,y=70,width=103,height=30)

        Poso_kartas=tk.Label(x)
        ft = tkFont.Font(family='Times',size=10)
        Poso_kartas["font"] = ft
        Poso_kartas["fg"] = "#333333"
        Poso_kartas["justify"] = "center"
        Poso_kartas["text"] = p.card
        Poso_kartas.place(x=140,y=100,width=113,height=30)

        Poso_entry=tk.Entry(x)
        Poso_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Poso_entry["font"] = ft
        Poso_entry["fg"] = "#333333"
        Poso_entry["justify"] = "center"
        Poso_entry["text"] = "Ποσό"
        Poso_entry.place(x=40,y=320,width=131,height=30)

        Select_box=tkk.Combobox(x, state="readonly")
        Select_box['values'] = ('Μετρητά', 'Κάρτα')
        ft = tkFont.Font(family='Times',size=10)
        Select_box["font"] = ft
        Select_box["justify"] = "center"
        Select_box.place(x=40,y=400,width=131,height=30)

        Prosth_but=tk.Button(x)
        Prosth_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Prosth_but["font"] = ft
        Prosth_but["fg"] = "#000000"
        Prosth_but["justify"] = "center"
        Prosth_but["text"] = "Προσθήκη"
        Prosth_but.place(x=250,y=360,width=125,height=34)
        Prosth_but["command"] = Prosth_but_command



        Metakul_but=tk.Button(x)
        Metakul_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Metakul_but["font"] = ft
        Metakul_but["fg"] = "#000000"
        Metakul_but["justify"] = "center"
        Metakul_but["text"] = "Μετακύλιση ποσού"
        Metakul_but.place(x=300,y=80,width=120,height=30)
        Metakul_but["command"] = lambda:[Metakul_but_command(x, Poso_kartas, Poso_metrhta)]



        
        Oria_but=tk.Button(x)
        Oria_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Oria_but["font"] = ft
        Oria_but["fg"] = "#000000"
        Oria_but["justify"] = "center"
        Oria_but["text"] = "Προσθήκη Ορίων"
        Oria_but.place(x=700,y=550,width=200,height=34)
        Oria_but["command"] = lambda: Gui_oria(x)

        Poso_metrhta.config(text = p.cash)
        Poso_kartas.config(text = p.card)
