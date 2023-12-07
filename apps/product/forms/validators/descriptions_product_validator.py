from re import match


def description_product_validator(description, errors_list):
    pattern = r'(?=.*[a-zA-Z]{2,}).{,198}'
    if description and not match(pattern, str(description)):
        errors_list['description'] = 'Description invalid, please review it'
