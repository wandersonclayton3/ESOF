# gen_random_values.py
import random
import rstr
import datetime

def gen_age():
    return random.randint(15, 99)

def gen_cpf():
    return rstr.rstr('1234567890', 11)

def gen_phone():
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))
