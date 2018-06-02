from .exceptions import verify_type

class Insert:
    def __init__(self,table,fields):
        verify_type(table,'','table name')
        verify_type(fields,{},'fields')

        self.fields=fields
        self.table=table
    
    def to_sql(self):
        fields=''
        values=''
        for index,field in enumerate(self.fields.keys()):
            if index==0:
                fields=fields+field
                values=values+'"'+str(self.fields[field])+'"'
            else:
                fields=fields+','+field
                values=values+','+'"'+str(self.fields[field])+'"'
        return 'insert into {table} ({fields}) values ({values})'.format(table=self.table,fields=fields,values=values)