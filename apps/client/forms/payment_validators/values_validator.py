from re import match


def value_validator(value: float | str, errors_list: dict):
    if type(value) is str and not match(r'[0-9]{1,}', value):
        errors_list['value'] = 'Format value invalid, please review it'
