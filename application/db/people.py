from datetime import datetime as dt

def get_employees():
    today = dt.today().strftime('%d')
    if int(today) <= 15:
        workers = 15
    else:
        workers = 10
    return workers
