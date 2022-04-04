from DbHelper import DbHelper

class ProdottiDAO():
    __db = None
    
    def __init__(self):
       self.__db = DbHelper()
       
    def getprodotti_byannoattivazione(self):
     anno=input("Inserire l'anno di cui vuoi conoscere i prodotti attivati: ")
     richiesta=self.__db.query(f"""select * from prodotti where year(dataattivazione)={anno}""")
     return richiesta.fetchall()
    
    def getinproduzioneocommercio(self):
        listaprodotti=self.getprodotti_byannoattivazione()
        for prodotto in listaprodotti:
            if prodotto[2]==True or prodotto[3]==True:
                print(f'Idprodotto = {prodotto[0]}, Descrizione = {prodotto[1]}')
        return ''       
     

     

