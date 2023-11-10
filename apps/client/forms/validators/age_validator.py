from datetime import date as dt


def date_to_int(date: dt) -> int:
    date_str = str(date)
    y, m, d = date_str[:4], date_str[5:7], date_str[8:]
    return int(y + m + d)


def min_age(date, age, errors_list):
    date = date_to_int(date)
    current_date = date_to_int(dt.today())
    years = (current_date - date) / 10000
    if years < age:
        errors_list['birthday'] = 'Only adults can open account'
