import mysql.connector as mysql
from mysql.connector import Error
from config import config

class DbHelper:
    instance = None
    con = None
    def __new__(cls):
     if DbHelper.instance is None:
        DbHelper.instance = object.__new__(cls)
     return DbHelper.instance

    def __init__(self):
     __db_config = config['mysql']
     

     if DbHelper.con is None:
           
      try:
            DbHelper.con = mysql.connect(host = __db_config['host'], 
                database =__db_config['db'], user = __db_config['user'], 
                password = __db_config['password'])
            print('Connection succesful')
           
            
      except Error as e:
            print('Error: ', e)

    def query(self, query):   
        cursor=DbHelper.con.cursor()
        cursor.execute(query)
        return cursor

    def __del__(self):
     if DbHelper.con is not None:
        DbHelper.con.close()
        print('Database connection closed.')