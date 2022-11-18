import random


class PriceGenerator:
    def __init__(self):
        self.__prev_price = 0
        self.__price = 0

    def generate(self):
        self.__prev_price = self.__price
        self.__price = abs(self.__prev_price + random.randint(-5, 5))
        return self.__price

    def get_price(self):
        return self.__price
