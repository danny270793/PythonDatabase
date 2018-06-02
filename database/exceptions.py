class InvalidTypeException(Exception):
    pass

def verify_type(value,available,field):
    if not type(value) is type(available):
        raise InvalidTypeException('{field} must be {required} not {type}'.format(field=field,required=type(available),type=type(value)))