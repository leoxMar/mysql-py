from DbHelper import DbHelper

class FattureDAO():
    __db = None
    
    def __init__(self):
       self.__db = DbHelper()

    def getfattura_byiva(self):
       iva =input('Inserire iva delle fatture da cercare: ')
       richiesta = self.__db.query(f'select * from fatture where iva={iva}')
       risultato=richiesta.fetchall()
       return risultato
      

    def getfattureannuali_byiva(self):
        iva=input("Inserire l'iva di cui vuoi sapere le fatture annuali: ")
        richiesta= self.__db.query(f"select count(numerofattura),year(datafattura) from fatture where iva={iva} group by year(datafattura) ")
        risultato=richiesta.fetchall()
        for anno in risultato:
           print(f'Anno: {anno[1]}, numero di fatture: {anno[0]}')
        return ''   

    def countfatture(self):
        fatture=self.getfattura_byiva()
        return print(f'Numero di fatture: {len(fatture)}')
    
    def getimportifatture(self):
        richiesta= self.__db.query("select count(numerofattura),sum(importo),year(datafattura) from fatture group by year(datafattura)")
        risultato=richiesta.fetchall()
        for anno in risultato:
           print(f'Anno: {anno[2]}, numero di fatture: {anno[0]}, importo totale: {int(anno[1])}€')
    
    def getfattureannuali_bytipologia(self):
        tipologia=(input('Inserire la tipologia di cui vuoi sapere le fatture (a,b): ')).lower()
        richiesta=self.__db.query(f"select count(numerofattura),year(datafattura) from fatture where tipologia='{tipologia}' group by year(datafattura) ").fetchall()
        for anno in richiesta:
           print(f'Anno: {anno[1]} Numero di Fatture di tipo {tipologia}: {anno[0]}')
        return ''
    
    def getannialpiudiduefatture(self):
       listafatture=self.getfattureannualibytipologia()
       alpiu=[]
       for fattura in listafatture:
          if fattura[0]>2:
           alpiu.append(fattura[1])
       return alpiu   
       
    def getfatturandfornitore(self):
       richiesta=self.__db.query(('select fa.numerofattura,fa.importo,fa.iva,fa.datafattura,fo.denominazione from fatture fa,fornitori fo where fa.numerofornitore=fo.numerofornitore')).fetchall()
       for elemento in richiesta:
          print(f"Numero Fattura: {elemento[0]}, Importo: {elemento[1]}€, Iva: {elemento[2]}%, Data: {elemento[3]}, Fornitore: {elemento[4]}. ")
       return ''
       
    def getimporti_byresidenza(self):
        residenza=input('Inserire La zona di cui vuoi le fatture in base ai clienti: ')
        richiesta= self.__db.query(f"""select sum(f.importo),c.regioneresidenza from fatture f,clienti c 
        where c.regioneresidenza='{residenza}'
        and c.numerocliente=f.idcliente
        group by c.regioneresidenza""")
        risultato=richiesta.fetchall()
        print(f"Località: {risultato[0][1]}, Somma degli importi: {risultato[0][0]}")
        return ''


