class Elegxos:
    def __init__(self, typos, poso_katax, typos_plir, katigoria, orio_katigorias, ypoloipo):
        self.typos = typos
        self.poso_katax = poso_katax
        self.typos_plir = typos_plir
        self.katigoria = katigoria
        self.orio_katigorias = orio_katigorias
        self.ypoloipo = ypoloipo
    def create_diadikasia_elegxou(self):


        if (self.typos == "metakulish"):
            if((self.typos_plir == "Μετρητά") & (int(self.orio_katigorias) - int(self.poso_katax) >0)):
                return 1
            if ((self.typos_plir == "Κάρτα") & (int(self.ypoloipo) - int(self.poso_katax) >0)):
                return 1
            else:
                return 0

        

        if ((self.ypoloipo - int(self.poso_katax) >= 0) & (int(self.orio_katigorias) - int(self.poso_katax) >= 0)):#h sunalagh einai epituxhs
            return 0
        elif(self.ypoloipo - int(self.poso_katax) < 0): #aneparkhs upoloipo
            return 1
        elif(int(self.orio_katigorias) - int(self.poso_katax) < 0): #aneparkhs oria
            return 2
