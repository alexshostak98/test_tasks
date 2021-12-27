"""
Написать функцию декоратор печатающую в файл дату и время момента декорирования функции и имя функции, и при каждом
вызове функции печатать дату и время момента вызова функции и имя функции
"""

from datetime import datetime


def get_log_message(func) -> str:
    return f"{datetime.isoformat(datetime.now())}#{func.__name__}\n"


def deco_func(func):
    with open("deco", "a", encoding="UTF-8") as file:
        file.write(get_log_message(func))

    def wrapper():
        print(get_log_message(func))
        func()

    return wrapper

# @deco_func
# def fun():
#     pass
#
#
# count = 5
# while count:
#     fun()
#     count -= 1
