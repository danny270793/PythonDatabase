from .exceptions import verify_type

class Select:
    
    @staticmethod
    def validate_fields(fields):
        if type(fields) is str:
            fields=(fields,)
        return fields
    
    @staticmethod 
    def validate_conditions(conditions):
        if len(conditions)==0:
            return ()
        
        isTuple=False
        for condition in conditions:
            if type(condition) is tuple:
                isTuple=True
        if not isTuple:
            conditions=(conditions,)
        return conditions
    
    def __init__(self,table,fields,conditions=()):
        fields=Select.validate_fields(fields)
        conditions=Select.validate_conditions(conditions)
        
        verify_type(table,'','table name')
        verify_type(fields,(),'fields')
        verify_type(conditions,(),'conditions')

        self.fields=fields
        self.conditions=conditions
        self.table=table
        
    def to_sql(self):
        fields=''
        conditions=''
        for index,field in enumerate(self.fields):
            if index==0:
                fields=fields+field
            else:
                fields=fields+','+field
        for index,condition in enumerate(self.conditions):
            if len(condition)==3:
                concatenator='or'
                field=condition[0]
                comparator=condition[1]
                value=str(condition[2])
            elif len(condition)==4:
                concatenator=condition[0]
                field=condition[1]
                comparator=condition[2]
                value=str(condition[3])

            if index==0:
                conditions=conditions+field+comparator+'"'+value+'"'
            else:
                conditions=conditions+' '+concatenator+' '+field+comparator+'"'+value+'"'
        if conditions=='':
            return 'select {fields} from {table}'.format(fields=fields,table=self.table)
        else:
            return 'select {fields} from {table} where {conditions}'.format(fields=fields,table=self.table,conditions=conditions)