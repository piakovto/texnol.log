import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as tkk
import datetime
import pickle
import portof as pp

class Kataxorisi:
        def __init__(self, typos, poso_katax, typos_plir, katigoria, imerominia):
                self.typos = typos
                self.poso_katax = poso_katax
                self.typos_plir = typos_plir
                self.katigoria = katigoria
                self.imerominia = imerominia

        def send(self, portof, aithma):
                return portof.tess(aithma)
p1 = Kataxorisi("", "", "", "", "")



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




def Gui_katax(x):


        def popup_epituxias():
                epituxia = tk.Toplevel(x)
                epituxia.title("Επιβεβαίωση Συναλλαγής")
                epituxia.geometry("300x200")
                epituxia.resizable(width=False, height=False)

                popup_text=tk.Label(epituxia)
                ft = tkFont.Font(family='Times',size=12)
                popup_text["font"] = ft
                popup_text["fg"] = "#333333"
                popup_text["justify"] = "center"
                popup_text["text"] = "Επιτυχημένη συναλλαγή!"
                popup_text.place(x=20,y=10,width=280,height=80)       
        def popup_apotuxias(res):
                if (res == 1): a = "Υπόλοιπο"
                elif(res == 2): a = "Υπόλοιπο ορίων"
                apotuxia = tk.Toplevel(x)
                apotuxia.title("Επιβεβαίωση Συναλλαγής")
                apotuxia.geometry("300x200")
                apotuxia.resizable(width=False, height=False)

                popup_text=tk.Label(apotuxia)
                ft = tkFont.Font(family='Times',size=12)
                popup_text["font"] = ft
                popup_text["fg"] = "#333333"
                popup_text["justify"] = "center"
                popup_text["text"] = "Ανεπαρκές " + a
                popup_text.place(x=20,y=10,width=280,height=80)       
        def But_yes(ai):
                temp = ai.send(pp.p, ai)
                if (temp == 0 or temp == 3): popup_epituxias()
                elif(temp == 1 or temp == 2): popup_apotuxias(temp)
        def popup_epivevaiosis(ait):
                W_epivevaiosis = tk.Toplevel(x)
                W_epivevaiosis.title("Επιβεβαίωση Συναλλαγής")
                W_epivevaiosis.geometry("300x200")
                W_epivevaiosis.resizable(width=False, height=False)

                B_yes=tk.Button(W_epivevaiosis)
                B_yes["bg"] = "#efefef"
                ft = tkFont.Font(family='Times',size=10)
                B_yes["font"] = ft
                B_yes["fg"] = "#000000"
                B_yes["justify"] = "center"
                B_yes["text"] = "Επιβεβαίωση"
                B_yes.place(x=20,y=130,width=80,height=25)
                B_yes["command"] = lambda: [But_yes(ait), W_epivevaiosis.destroy()]

                B_no=tk.Button(W_epivevaiosis)
                B_no["bg"] = "#efefef"
                ft = tkFont.Font(family='Times',size=10)
                B_no["font"] = ft
                B_no["fg"] = "#000000"
                B_no["justify"] = "center"
                B_no["text"] = "Ακύρωση"
                B_no.place(x=200,y=130,width=80,height=25)
                B_no["command"] = lambda: [W_epivevaiosis.destroy()]

                popup_text=tk.Label(W_epivevaiosis)
                ft = tkFont.Font(family='Times',size=12)
                popup_text["font"] = ft
                popup_text["fg"] = "#333333"
                popup_text["justify"] = "center"
                popup_text["text"] = "Συναλλαγή "+p1.poso_katax+" ευρώ με "+p1.typos_plir
                popup_text.place(x=20,y=10,width=280,height=80)       
        
        def create_kataxor_command(typos, poso, typos_plir, kathg):
                p1 = Kataxorisi(typos, poso, typos_plir, kathg, datetime.datetime.now().strftime("%x %X \n"))
                popup_epivevaiosis(p1)


        
        def esoda():        
                for widget in x.winfo_children():
                              widget.destroy()
                
                poso_katax_entry=tk.Entry(x)
                poso_katax_entry["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times',size=10)
                poso_katax_entry["font"] = ft
                poso_katax_entry["fg"] = "#333333"
                poso_katax_entry["justify"] = "center"
                poso_katax_entry["text"] = "Ποσό"
                poso_katax_entry.place(x=390,y=100,width=139,height=30)



                Select_box_payment=tkk.Combobox(x, state="readonly")
                Select_box_payment['values'] = ('Μετρητά', 'Κάρτα')
                ft = tkFont.Font(family='Times',size=10)
                Select_box_payment["font"] = ft
                Select_box_payment["justify"] = "center"
                Select_box_payment.place(x=390,y=280,width=100,height=30)

                create_kataxor=tk.Button(x)
                create_kataxor["bg"] = "#efefef"
                ft = tkFont.Font(family='Times',size=10)
                create_kataxor["font"] = ft
                create_kataxor["fg"] = "#000000"
                create_kataxor["justify"] = "center"
                create_kataxor["text"] = "Καταχώρηση"
                create_kataxor.place(x=400,y=380,width=105,height=34)
                create_kataxor["command"] = lambda: [create_kataxor_command(1, poso_katax_entry.get(), Select_box_payment.get(), 1)]


        def eksoda():
                for widget in x.winfo_children():
                              widget.destroy()
                
                poso_katax_entry=tk.Entry(x)
                poso_katax_entry["borderwidth"] = "1px"
                ft = tkFont.Font(family='Times',size=10)
                poso_katax_entry["font"] = ft
                poso_katax_entry["fg"] = "#333333"
                poso_katax_entry["justify"] = "center"
                poso_katax_entry["text"] = "Ποσό"
                poso_katax_entry.place(x=390,y=100,width=139,height=30)

                categ=[]
                tkvar = tk.StringVar(x)
                for k,v in categories.items():
                    categ.append(k)
                    categ.extend(v)
                Select_box_categor = tk.OptionMenu(x, tkvar, *categ)
                for i in categories:
                        Select_box_categor['menu'].entryconfigure(i, state = "disabled",font=('arial italic',11))
                Select_box_categor.place(x=390,y=190,width=100,height=30)


                Select_box_payment=tkk.Combobox(x, state="readonly")
                Select_box_payment['values'] = ('Μετρητά', 'Κάρτα')
                ft = tkFont.Font(family='Times',size=10)
                Select_box_payment["font"] = ft
                Select_box_payment["justify"] = "center"
                Select_box_payment.place(x=390,y=280,width=100,height=30)

                create_kataxor=tk.Button(x)
                create_kataxor["bg"] = "#efefef"
                ft = tkFont.Font(family='Times',size=10)
                create_kataxor["font"] = ft
                create_kataxor["fg"] = "#000000"
                create_kataxor["justify"] = "center"
                create_kataxor["text"] = "Καταχώρηση"
                create_kataxor.place(x=400,y=380,width=105,height=34)
                create_kataxor["command"] = lambda: [create_kataxor_command(0, poso_katax_entry.get(), Select_box_payment.get(), tkvar.get())]


        
        def next_screen(y):
                if (y == "Έσοδα"):
                        esoda()
                elif (y == "Έξοδα"):
                        eksoda()
        
        GLabel_299=tk.Label(x)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_299["font"] = ft
        GLabel_299["fg"] = "#333333"
        GLabel_299["justify"] = "center"
        GLabel_299["text"] = "Θέλω να καταχωρήσω:"
        GLabel_299.place(x=150,y=150,width=218,height=30)

        Select_katxor=tkk.Combobox(x, state="readonly")
        Select_katxor['values'] = ('Έσοδα', 'Έξοδα')
        ft = tkFont.Font(family='Times',size=10)
        Select_katxor["font"] = ft
        Select_katxor["justify"] = "center"
        Select_katxor.place(x=180,y=200,width=100,height=30)
       
        Next_but=tk.Button(x)
        Next_but["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Next_but["font"] = ft
        Next_but["fg"] = "#000000"
        Next_but["justify"] = "center"
        Next_but["text"] = "Επόμενο"
        Next_but.place(x=150,y=265,width=200,height=35)
        Next_but["command"] = lambda: next_screen(Select_katxor.get())


