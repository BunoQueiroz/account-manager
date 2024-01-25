from re import match


def name_product_validator(name: str, errors_list):
    pattern = r'^[a-zA-ZáàãâÁÀÃÂéêÉÊóõôÓÕÔúÚçÇ0-9\s-]{2,70}$'
    if not match(pattern, str(name)):
        errors_list['name'] = 'Name invalid, please review it'
