import sqlite3
from .drop import Drop
from .create import Create
from .insert import Insert
from .select import Select
from .update import Update

class Sqlite:

    @staticmethod
    def rows_to_dict(fields,rows):
        if type(fields) is str:
            fields=(fields,)
        
        registers=[]
        for row in rows:
            register={}
            for index,column in enumerate(row):
                register[fields[index]]=column
            registers.append(register)
        return registers

    def __init__(self,path):
        self.path=path
        self.database=sqlite3.connect(self.path)
        self.cursor=self.database.cursor()
        self.debuggable=False
    
    def __del__(self):
        self.database.close()

    def set_debuggable(self,debuggable=True):
        self.debuggable=debuggable
    
    def query(self,sql):
        if self.debuggable:
            print(sql)
        self.cursor.execute(sql)
        self.database.commit()
        return self.cursor.fetchall()
    
    def drop(self,table):
        drop=Drop(table)
        return self.query(drop.to_sql())

    def create(self,table,fields):
        create=Create(table,fields)
        return self.query(create.to_sql())
    
    def select(self,table,fields,conditions=[]):
        select=Select(table,fields,conditions)
        rows=self.query(select.to_sql())
        return Sqlite.rows_to_dict(fields,rows)
    
    def insert(self,table,fields):
        insert=Insert(table,fields)
        return self.query(insert.to_sql())
    
    def update(self,table,fields,conditions=[]):
        update=Update(table,fields,conditions)
        rows=self.query(update.to_sql())
        return Sqlite.rows_to_dict(fields,rows)

    def __str__(self):
        return str({'path':self.path})