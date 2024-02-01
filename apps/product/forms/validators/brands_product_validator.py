from re import match


def brand_product_validator(brand, errors_list):
    pattern = r'^(?=.*[a-zA-Z]{2,})[a-zA-Z0-9\sáãâàÁÃÂÀéêÉÊíÍóôÓÔúÚçÇ-]{2,50}$'
    if brand and not match(pattern, brand):
        errors_list['brand'] = 'Brand inválid, please review it'
