from re import match


def payer_validator(payer_name, errors_list: dict):
    pattern = r'^[a-zA-ZãáàâÃÁÀÂéêÉÊíÍóôÓÔúÚçÇ\s]{2,100}$'
    if type(payer_name) is not str or not match(pattern, payer_name):
        errors_list['payer'] = 'Payer name invalid, please review it'
