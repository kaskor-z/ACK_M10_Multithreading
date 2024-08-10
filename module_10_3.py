from threading import Thread, Lock
from time import sleep
from random import randint


class Bank():

    def __init__(self):
        self.balance = 0
        self.lock_1 = Lock()

    def deposit(self):
        for i in range(1, 100):
            deposit_ = randint(50, 500)
            self.balance += deposit_
            print(f'Пополнение: {deposit_}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock_1.locked():
                self.lock_1.release()
            sleep(0.001)

    def take(self):
        for item in range(1, 100):
            withdraw = randint(50, 500)
            print(f'Запрос на {withdraw}')
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f'Снятие: {withdraw}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock_1.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
