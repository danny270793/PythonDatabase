from .exceptions import verify_type

class Create:
    def __init__(self,table,fields):
        verify_type(table,'','table name')
        verify_type(fields,{},'fields')

        self.fields=fields
        self.table=table

    def to_sql(self):
        fields=''
        for index,field in enumerate(self.fields.keys()):
            if index==0:
                fields=fields+field+' '+self.fields[field]
            else:
                fields=fields+','+field+' '+self.fields[field]
        return 'create table {table} ({fields})'.format(table=self.table,fields=fields)