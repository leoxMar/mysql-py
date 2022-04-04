from ClientiDAO import ClientiDAO
from FattureDAO import FattureDAO
from ProdottiDAO import ProdottiDAO

class Test(object):
    __db = None
    
    def __init__(self):
       __clientidao = ClientiDAO()
       __fatturedao = FattureDAO() 
       __prodottidao= ProdottiDAO()
       #Esercizio 1
       #__clientidao.getclienti_bydata()
       #Esercizio 2 (Alajuela,Texas)
       #__clientidao.getcliente_byregione()
       #Esercizio 3
       #__fatturedao.countfatture()
       #Esercizio 4
       #__fatturedao.getimportifatture()
       #Esercizio 5
       #__prodottidao.getinproduzioneocommercio()
       #Esercizio 6
       #__fatturedao.getfattureannuali_byiva()
       #Esercizio 7
       #__fatturedao.getfattureannuali_bytipologia()
       #Esercizio 8
       #__fatturedao.getfatturandfornitore()
       #Esercizio 9(Alajuela,Texas)
       #__fatturedao.getimporti_byresidenza()
       #Esercizio 10(Tutte le fatture nel database partono da 50€)
       #__clientidao.getclienti_byspesae_byanno()

test=Test()