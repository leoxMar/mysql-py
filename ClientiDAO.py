from DbHelper import DbHelper

class ClientiDAO():
    __db = None
    
    def __init__(self):
       self.__db = DbHelper()

    def getclienti_bydata(self):
       anno=input('Inserire anno di nascita dei clienti che vuoi cercare: ')
       richiesta = self.__db.query(f'select nome,cognome from clienti where year(datanascita)={anno}')
       risultato=richiesta.fetchall()
       for cliente in risultato:
        print(f"Nome: {cliente[0]}, Cognome: {cliente[1]}")
       return ''
       
    def getcliente_byregione(self):
       regione=input('Inserire regione dei clienti da cercare: ')
       richiesta = self.__db.query(f"SELECT nome, cognome FROM clienti where regioneresidenza='{regione}'")
       risultato=richiesta.fetchall()
       for i in range(len(risultato)):
          nome=risultato[i][0]
          cognome=risultato[i][1]
          denominazione=f'Denominazione: {nome}-{cognome} '
          print(denominazione)
          
    def getclienti_byspesae_byanno(self):
          anno=input('Inserire anno di nascita dei clienti: ')
          importomin=input("Inserisci l'importo minimo di spesa: ")
          richiesta=self.__db.query(f""" select count(*)  from(select idcliente from fatture f ,
          (SELECT numerocliente FROM clienti where year(datanascita)={anno}) as c
           where f.idcliente=c.numerocliente and f.importo>{importomin} group by idcliente)as t""").fetchall()
          print(f"Anno: {anno}, Numero di clienti: {richiesta[0][0]}")
          return '' 


       

               




