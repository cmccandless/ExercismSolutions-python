from random import randint, seed
from time import perf_counter


def rndChr():
    return chr(randint(ord('A'), ord('Z')))


class Robot:
    def __init__(self):
        seed(perf_counter())
        self.name = None
        self.reset()

    def reset(self):
        seed(perf_counter())
        self.name = '{}{}{:03}'.format(rndChr(), rndChr(), randint(0, 999))
