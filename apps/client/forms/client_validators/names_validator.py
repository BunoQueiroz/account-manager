from re import match


def first_name_validator(first_name, errors_lits):
    pattern = r'^[a-zA-Z\sâáãÂÁÃéêÉÊíîÍÎóôÓÔúÚñÑçÇ]{2,30}$'
    if not match(pattern, first_name):
        errors_lits['first_name'] = 'First name invalid'


def last_name_validator(last_name, erros_list):
    pattern = r'^[a-zA-Z\sâáãÂÁÃéêÉÊíîÍÎóôÓÔúÚñÑçÇ]{2,70}$'
    if last_name and not match(pattern, last_name):
        erros_list['last_name'] = 'Last name invalid'

