from threading import Thread
from time import sleep

COUNT_ENEMIES = 100


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        c_enemis, i = COUNT_ENEMIES, 0
        print(f'  {self.name}, на нас напали!')
        while c_enemis > 0:
            c_enemis -= self.power
            i += 1
            sleep(1)
            print(f' {self.name} сражается {i}..., осталось {c_enemis} воинов.')
        print(f'\n****** {self.name} одержал победу спустя {i} дней(дня)!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
