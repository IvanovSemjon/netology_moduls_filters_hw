from datetime import datetime as dt
from application import salary
from application.db import people
from application.db.config import NAME, PASSWORD


get_employees = people.get_employees()
calculate_salary = salary.calculate_salary()

class Hr:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def main():
    hr = Hr(NAME, PASSWORD)
    print(f"Good morning {hr.name}, Какая разнарядка на сегодняшний день?")

    while True:
        command = input('Введите команду: ')
        if command == 'p':
            print(f"на сегодняшний день нам необходимо {get_employees} рабочих.")
            print(f"Информация актуальна на '{dt.now().strftime('%d.%m.%Y')}'.")
        if command == 's':
            print(f"До конца месяца зарплата одного рабочего составит {calculate_salary} рублей.")
            print(f"Информация актуальна на '{dt.now().strftime('%d.%m.%Y')}'.")
        if command == 't':
            result = get_employees * calculate_salary
            print(f"До конца месяца нам нужно {get_employees} рабочих и их общая зарплата составит {result} рублей.")
            print(f"Информация актуальна на '{dt.now().strftime('%d.%m.%Y')}'.")
        if command == 'e':
            break


if __name__ == '__main__':
    main()