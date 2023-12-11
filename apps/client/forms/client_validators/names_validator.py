from re import match


def name_invalid(first_name):
    pattern = r'^[a-zA-Z\sâáãÂÁÃéêÉÊíîÍÎóôÓÔúÚñÑ]{2,30}$'
    return False if match(pattern, first_name) else True


def first_name_validator(first_name, errors_lits):
    if name_invalid(first_name):
        errors_lits['first_name'] = 'First name invalid'


def last_name_validator(last_name, erros_list):
    if last_name and name_invalid(last_name):
        erros_list['last_name'] = 'Last name invalid'

