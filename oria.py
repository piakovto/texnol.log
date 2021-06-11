import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as tkk
import pickle

class Oria:
    def __init__(self, spiti, car, educat, doctor, fun, etc):
        self.spiti = spiti
        self.car = car
        self.educat = educat
        self.doctor = doctor
        self.fun = fun
        self.etc = etc
    def save_oria(self):
                fl = open("oria", "wb")
                pickle.dump(self, fl)
                fl.close()

orio = Oria(0,0,0,0,0,0)

fl = open("oria", "rb")
orio = pickle.load(fl)
fl.close()
def Gui_oria(x):
    def change_orio(poso, cathg):
        if (cathg == "ΣΠΙΤΙ"):
                orio.spiti = poso
        elif (cathg ==  "ΑΥΤΟΚΙΝΗΤΟ"):
                orio.car = poso
        elif (cathg == "ΕΚΠΑΙΔΕΥΣΗ"):
                orio.educat = poso
        elif (cathg == "ΙΑΤΡΙΚΑ"):
                orio.doctor = poso
        elif (cathg == "ΔΙΑΣΚΕΔΑΣΗ"):
                orio.fun = poso
        elif (cathg == "ΔΙΑΦΟΡΑ"):
                orio.etc = poso
        orio.save_oria()
    def popup_epivevaiosis_oria(oria_window, poso, categ):

        temp_check = int(poso)
        if (temp_check > 0):
            W_epivevaiosis_orio = tk.Toplevel(x)
            W_epivevaiosis_orio.title("Επιβεβαίωση Ορίου")
            W_epivevaiosis_orio.geometry("400x200")
            W_epivevaiosis_orio.resizable(width=False, height=False)

            But_yes=tk.Button(W_epivevaiosis_orio)
            But_yes["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            But_yes["font"] = ft
            But_yes["fg"] = "#000000"
            But_yes["justify"] = "center"
            But_yes["text"] = "Επιβεβαίωση"
            But_yes.place(x=20,y=130,width=80,height=25)
            But_yes["command"] = lambda: [W_epivevaiosis_orio.destroy(), change_orio(poso, categ), popup_completion(oria_window)]

            But_no=tk.Button(W_epivevaiosis_orio)
            But_no["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            But_no["font"] = ft
            But_no["fg"] = "#000000"
            But_no["justify"] = "center"
            But_no["text"] = "Ακύρωση"
            But_no.place(x=200,y=130,width=80,height=25)
            But_no["command"] = lambda: [print("akyro"), W_epivevaiosis_orio.destroy(), popup_cancel(oria_window)]

            popup_text2=tk.Label(W_epivevaiosis_orio)
            ft = tkFont.Font(family='Times',size=12)
            popup_text2["font"] = ft
            popup_text2["fg"] = "#333333"
            popup_text2["justify"] = "center"
            popup_text2["text"] = "Αλλαγή ποσού ορίου " + categ + " σε " + poso
            popup_text2.place(x=20,y=10,width=350,height=80)
        elif(temp_check < 0):
            popup_fail()

    def popup_completion(oria_window):
        W_popup_completion = tk.Toplevel(x)
        W_popup_completion.title("Μήνυμα")
        W_popup_completion.geometry("300x200")
        W_popup_completion.resizable(width=False, height=False)

        But_ok=tk.Button(W_popup_completion)
        But_ok["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        But_ok["font"] = ft
        But_ok["fg"] = "#000000"
        But_ok["justify"] = "center"
        But_ok["text"] = "ΟΚ"
        But_ok.place(x=120,y=130,width=80,height=25)
        But_ok["command"] = lambda: [W_popup_completion.destroy(), refresh_oria(oria_window)]
 
        popup_text2=tk.Label(W_popup_completion)
        ft = tkFont.Font(family='Times',size=12)
        popup_text2["font"] = ft
        popup_text2["fg"] = "#333333"
        popup_text2["justify"] = "center"
        popup_text2["text"] = "Επιτυχής ενέργεια"
        popup_text2.place(x=20,y=10,width=280,height=80)

    def popup_cancel(oria_window):
        W_popup_cancel = tk.Toplevel(x)
        W_popup_cancel.title("Μήνυμα")
        W_popup_cancel.geometry("300x200")
        W_popup_cancel.resizable(width=False, height=False)

        But_ok=tk.Button(W_popup_cancel)
        But_ok["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        But_ok["font"] = ft
        But_ok["fg"] = "#000000"
        But_ok["justify"] = "center"
        But_ok["text"] = "ΟΚ"
        But_ok.place(x=120,y=130,width=80,height=25)
        But_ok["command"] = lambda: [W_popup_cancel.destroy(), refresh_oria(oria_window)]
 
        popup_text2=tk.Label(W_popup_cancel)
        ft = tkFont.Font(family='Times',size=12)
        popup_text2["font"] = ft
        popup_text2["fg"] = "#333333"
        popup_text2["justify"] = "center"
        popup_text2["text"] = "Η ενέργεια ακυρώθηκε"
        popup_text2.place(x=20,y=10,width=280,height=80) 

    def popup_fail():
        
        W_popup_fail = tk.Toplevel(x)
        W_popup_fail.title("Μήνυμα")
        W_popup_fail.geometry("300x200")
        W_popup_fail.resizable(width=False, height=False)

        But_ok_fail=tk.Button(W_popup_fail)
        But_ok_fail["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        But_ok_fail["font"] = ft
        But_ok_fail["fg"] = "#000000"
        But_ok_fail["justify"] = "center"
        But_ok_fail["text"] = "ΟΚ"
        But_ok_fail.place(x=120,y=130,width=80,height=25)
        But_ok_fail["command"] = lambda: [print("fail"), W_popup_fail.destroy()]

        
        W_popup_fail_label=tk.Label(W_popup_fail)
        ft = tkFont.Font(family='Times',size=12)
        W_popup_fail_label["font"] = ft
        W_popup_fail_label["fg"] = "#333333"
        W_popup_fail_label["justify"] = "center"
        W_popup_fail_label["text"] = "Λάθος είσοδος στοιχείων"
        W_popup_fail_label.place(x=20,y=10,width=280,height=80)    


    def main_gui_oria(x):

        oria_window = tk.Toplevel(x)
        oria_window.title("Επξεργασία Ορίων")
        oria_window.geometry("950x625")
        oria_window.resizable(width=False, height=False)

        
        Ltext1=tk.Label(oria_window)
        ft = tkFont.Font(family='Times',size=12)
        Ltext1["font"] = ft
        Ltext1["fg"] = "#333333"
        Ltext1["justify"] = "center"
        Ltext1["text"] = "Θέλω να θέσω όριο στην εξής κατηγορία:"
        Ltext1.place(x=150,y=350,width=300,height=30)

        Select_katig=tkk.Combobox(oria_window, state="readonly")
        Select_katig['values'] = ('ΣΠΙΤΙ', 'ΑΥΤΟΚΙΝΗΤΟ', 'ΕΚΠΑΙΔΕΥΣΗ', 'ΙΑΤΡΙΚΑ', 'ΔΙΑΣΚΕΔΑΣΗ', 'ΔΙΑΦΟΡΑ')
        ft = tkFont.Font(family='Times',size=10)
        Select_katig["font"] = ft
        Select_katig["justify"] = "center"
        Select_katig.place(x=180,y=400,width=120,height=30)

        Ltext2=tk.Label(oria_window)
        ft = tkFont.Font(family='Times',size=12)
        Ltext2["font"] = ft
        Ltext2["fg"] = "#333333"
        Ltext2["justify"] = "center"
        Ltext2["text"] = "Χρηματικό Όριο:"
        Ltext2.place(x=110,y=450,width=218,height=30)

        orio_entry=tk.Entry(oria_window)
        orio_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        orio_entry["font"] = ft
        orio_entry["fg"] = "#333333"
        orio_entry["justify"] = "center"
        orio_entry["text"] = "Ποσό"
        orio_entry.place(x=180,y=500,width=139,height=30)    
       
        Next_but2=tk.Button(oria_window)
        Next_but2["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Next_but2["font"] = ft
        Next_but2["fg"] = "#000000"
        Next_but2["justify"] = "center"
        Next_but2["text"] = "Επόμενο"
        Next_but2.place(x=250,y=580,width=200,height=35)
        Next_but2["command"] = lambda: [popup_epivevaiosis_oria(oria_window, orio_entry.get(), Select_katig.get())]
        refresh_oria(oria_window)
    def refresh_oria(window):
        with (open("oria", "rb")) as f:
                while True:
                        try:
                                a = (pickle.load(f))
                        except EOFError:
                                break

        f.close()
        
        
        listbox = tk.Listbox(window)
        listbox.place(x=30,y=20,width=800,height=200)

        count = 0;
        categ_list = ["ΣΠΙΤΙ", "ΑΥΤΟΚΙΝΗΤΟ", "ΕΚΠΑΙΔΕΥΣΗ", "ΙΑΤΡΙΚΑ", "ΔΙΑΣΚΕΔΑΣΗ", "ΔΙΑΦΟΡΑ"]

        for attr, value in a.__dict__.items():
            s = categ_list[count] + " " + str(value)
            count += 1         
            listbox.insert(count, s)
        s = ""



    main_gui_oria(x)
