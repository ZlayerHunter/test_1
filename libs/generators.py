from .order import Order
from .courier import Courier
import random

def gen_geo():
    randfloat = random.uniform
    return [randfloat(61.97, 62.08), randfloat(129.65, 129.76)]

def generate_order():
    randint = random.randint
    start = gen_geo()
    end = gen_geo()
    cost = randint(1, 1000)
    return Order(start, end, cost)


def generate_courier():
    point = gen_geo()
    return Courier(point)
