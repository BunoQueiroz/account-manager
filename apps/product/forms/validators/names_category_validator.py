from re import match


def name_category_validator(name_category, errors_list):
    pattern = r'^[a-zA-ZáâãàÁÂÃÀéêÉÊíÍóôÓÔúÚçÇ\s]{2,50}$'
    if not match(pattern, str(name_category)):
        errors_list['name'] = 'Name invalid, please review it'
