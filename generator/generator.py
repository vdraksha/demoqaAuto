import random

from data.data import Person
from faker import Faker


faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    """Генерирует и возвращает данные для класса Person в data через faker.
    """
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        email=faker_ru.email(),
        first_name=faker_ru.first_name()[:25],
        last_name=faker_ru.last_name()[:25],
        age=random.randint(18, 99),
        salary=random.randint(16000, 250000),
        department=faker_ru.job()[:25],
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
