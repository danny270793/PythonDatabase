from .exceptions import verify_type

class Drop:
    def __init__(self,table):
        verify_type(table,'','table name')
        
        self.table=table

    def to_sql(self):
        return 'drop table if exists {table}'.format(table=self.table)