import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as tkk
import datetime
import pickle

class Kataxorisi:
        def __init__(self, typos, poso_katax, typos_plir, katigoria, imerominia):
                self.typos = typos
                self.poso_katax = poso_katax
                self.typos_plir = typos_plir
                self.katigoria = katigoria
                self.imerominia = imerominia
p1 = Kataxorisi("", "", "", "", "")

def create_kataxor_command(typos, poso, typos_plir, kathg):
        p1 = Kataxorisi(typos, poso, typos_plir, kathg, datetime.datetime.now().strftime("%x %X \n"))
        print (p1.poso_katax)
        
def Gui_katax(x):

        def esoda():
                '''def create_kataxor_command():
                        #f = open("istoriko.txt", "a")
                        #f.write("1, ")
                        #f.write(poso_katax_entry.get() + ", ")
                        #f.write(Select_box_payment.get() + ", ")
                        #x = datetime.datetime.now()
                        #f.write(x.strftime("%x %X \n"))
                        #f.close()
                        p1.typos = "1"
                        p1.poso_katax = poso_katax_entry.get()
                        p1.typos_plir = Select_box_payment.get()
                        p1.katigoria = ""
                        p1.imerominia = (datetime.datetime.now().strftime("%x %X \n"))
                        print(p1.typos)
                        print(p1.poso_katax)
                        print(p1.typos_plir)
                        print(p1.katigoria)
                        print(p1.imerominia)
                        fl = open("qwerty", "ab")
                        pickle.dump(p1, fl)
                        fl.close()
                        objects = []
                        with (open("qwerty", "rb")) as f1:
                            while True:
                                try:
                                    objects.append(pickle.load(f1))
                                except EOFError:
                                    break
                        print(objects[0].poso_katax)
                        print(objects[0].typos_plir)
                        print(objects[1].poso_katax)
                        print(objects[1].typos_plir)
                        print(len(objects))       
                        fl.close()'''
                        
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
                create_kataxor["command"] = lambda: create_kataxor_command(1, poso_katax_entry.get(), Select_box_payment.get(), " ",)


        def eksoda():
                '''def create_kataxor_command():
                        #f = open("istoriko.txt", "a")
                        #f.write("1, ")
                        #f.write(poso_katax_entry.get() + ", ")
                        #f.write(Select_box_payment.get() + ", ")
                        #x = datetime.datetime.now()
                        #f.write(x.strftime("%x %X \n"))
                        #f.close()
                        p1.typos = "0"
                        p1.poso_katax = poso_katax_entry.get()
                        p1.typos_plir = Select_box_payment.get()
                        p1.katigoria = Select_box_categor.get()
                        x = datetime.datetime.now()
                        p1.imerominia = (x.strftime("%x %X \n"))
                        print(p1.typos)
                        print(p1.poso_katax)
                        print(p1.typos_plir)
                        print(p1.katigoria)
                        print(p1.imerominia)
                        fl = open("qwerty", "ab")
                        pickle.dump(p1, fl)
                        fl.close()
                        objects = []
                        with (open("qwerty", "rb")) as f1:
                            while True:
                                try:
                                    objects.append(pickle.load(f1))
                                except EOFError:
                                    break
                        print(objects[0].poso_katax)
                        print(objects[0].typos_plir)
                        print(objects[1].poso_katax)
                        print(objects[1].typos_plir)
                        print(len(objects))       
                        fl.close()'''

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

                Select_box_categor=tkk.Combobox(x, state="readonly")
                Select_box_categor['values'] = ('Ποτά', 'Φαι')
                ft = tkFont.Font(family='Times',size=10)
                Select_box_categor["font"] = ft
                Select_box_categor["justify"] = "center"
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
                create_kataxor["command"] = lambda: create_kataxor_command(0, poso_katax_entry.get(), Select_box_payment.get(), Select_box_categor)


        
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


