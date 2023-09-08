# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.

import logging

logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.INFO, filemode='w',
                    format='%(levelname)s -> %(asctime)s: %(message)s')
logger = logging.getLogger(__name__)

class NameVerification:
    def __set_name__(self, owner, name):
        self.par_name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.par_name)

    def __set__(self, instance, value: str):
        if not value.isalpha() or not value[0].isupper():
            raise ValueError(
                f'{self.par_name.capitalize()} должно начинаться с заглавной буквы и содержать только буквы')
        instance.__dict__[self.par_name] = value


class Student:
    first_name = NameVerification()
    patronymic = NameVerification()
    last_name = NameVerification()


    def __init__(self, first_name, patronymic, last_name):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name


    def __str__(self):
        return f'{self.first_name} {self.patronymic} {self.last_name}'

try:
    student = Student('ольга', 'Ивановна', 'Сергеева')
    print(student)
except ValueError as er:
    logger.error(f'Возникла такая ошибка: {er}')
    print(f"Ошибка: {er}")

try:
    student = Student('Ольга', 'Ивановна', 'Сергеева')
    print(student)
except ValueError as er:
    logger.error(f'Возникла такая ошибка: {er}')
    print(f"Ошибка: {er}")

try:
    student = Student('Ольга', '23!!', 'Сергеева')
    print(student)
except ValueError as er:
    logger.error(f'Возникла такая ошибка: {er}')
    print(f"Ошибка: {er}")

try:
    student = Student('Ольга', 'Ивановна', 'сергеева')
    print(student)
except ValueError as er:
    logger.error(f'Возникла такая ошибка: {er}')
    print(f"Ошибка: {er}")