from datetime import datetime as dt
from calendar import monthrange as mt


def calculate_salary():
    basic_salary_per_day = 2000
    today = dt.today()
    today_day = dt.today().strftime('%d')
    mounth = mt(today.year, today.month)[1]
    result_salary = (int(mounth) - int(today_day)) * basic_salary_per_day
    return result_salary


