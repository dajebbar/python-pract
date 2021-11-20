import sys
import psycopg2
from dict_app import *


class DBManagement:
    """[Setting up and interfacing a PostgreSQL database]
    """

    def __init__(self, dbName, user, passwd, host, port=5432):
        """[Establishing the connection - Creating the cursor]

        Args:
            dbName ([type]): [description]
            user ([type]): [description]
            passwd ([type]): [description]
            host ([type]): [description]
            port (int, optional): [description]. Defaults to 5432.
        """

        try:
            self.DataBase = psycopg2.connect(
                host=host, port=port, dbname=dbName, user=user, password=passwd)
        except Exception as err:
            print(
                f"Connection with the database failed\nError detected :\n{err}")
            self.fail = 1
        
        else:
            self.cursor = self.DataBase.cursor() # creation of cursor
            self.fail = 0
    

    def create_tables(self, dictTables):
        """[Creation of the tables described in the <dicTables> dictionary.]

        Args:
            dictTables ([type]): [description]
        """
        for table in dictTables:
            req = f"CREATE TABLE {table} ("
            pk = ''
            for descr in dictTables[table]:
                field_name, tch = descr
                if tch =='i':
                    type_field ='INTEGER'
                elif tch =='k':
                    type_field ='SERIAL'
                    pk = field_name
                else:
                    type_field = 'VARCHAR(tch)'
                req = req + f"{field_name} {type_field},"
            if pk == '':
                req = req[:-2] + '")'
            
            else:
                req = req + f"CONSTRAINT {pk}_pk PRIMARY KEY({pk}))"
    

    def drop_tables(self, dictTables):
        """[Delete all tables described in <dicTables>]

        Args:
            dictTables ([type]): [description]
        """
        for table in list(dictTables.keys()):
            req = f"DROP TABLE {table}"
            self.execute_req(req)
        self.commit()
    
    def execute_req(self, req, param =None):
        """[Execution of the <req> query, with possible error detection]

        Args:
            req ([type]): [description]
            param ([type], optional): [description]. Defaults to None.
        """
        try:
            self.cursor.executemany(req, param)
        except Exception as err:
            print(f"Bad SQL query\n{req}\nError detected: ")
            print(err)
            return 0
        else:
            return 1
    
    def req_result(self):
        """[returns the result of the previous query (a list of tuples)]
        """
        return self.cursor.fetchall()
    
    def commit(self):
        if self.DataBase:
            self.DataBase.commit()
    
    def close(self):
        if self.DataBase:
            self.DataBase.close()
