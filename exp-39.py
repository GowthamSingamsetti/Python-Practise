import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        print((first, second))


dice1 = Dice()
dice1.roll()
