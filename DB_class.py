import mysql.connector

class DB:
    def __init__(self,user, password, host_address, database_name):
        self.user= user
        self.password = password
        self.host_address = host_address
        self.database_name = database_name
        
    def __connect(self):
        self.conn = mysql.connector.connect(user=self.user, password=self.password,host=self.host_address, database=self.database_name)
        self.cur = self.conn.cursor()

    def __exit(self):
        self.cur.close()
        self.conn.close()
        
    def execute(self,sql:str):
        self.__connect()
        
        self.cur.execute(sql)
        result=self.cur.fetchall()
        self.conn.commit()
        
        self.__exit()
        
        return result
    

        

        

    
