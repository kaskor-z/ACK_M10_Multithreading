from threading import Thread
from random import randint
from time import sleep
from queue import Queue

class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self):
        self.queue = Queue()

    def guest_arrival():
        for guest in guests:
            for table in tables:
                if table.guest is None:
                    table.guest = guest.name
                    guest.start()
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    break
            if not guest.is_alive():
                cafe.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests():
        empty_table = True
        while not cafe.queue.empty() or empty_table:
            for table in tables:
                guest_name = table.guest
                for guest in guests:
                    if guest.name == guest_name:
                        if not guest.is_alive():
                            print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                            print(f'Стол номер {table.number} свободен')
                            table.guest = None
                            guest.join()
                            if not cafe.queue.empty():
                                guest = cafe.queue.get()
                                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                                table.guest = guest.name
                                guest.start()
                            # for table_ in tables: print('Стол №', table_.number, '-', table_.guest, ' ', end='')
                        break
            empty_table = False
            for table in tables:
                if not table.guest is None:
                    empty_table = True
                    break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
print(guests_names)
# Создание гостей
guests = [Guest(name) for name in guests_names]
print('-----------')
# Заполнение кафе столами
cafe = Cafe()
# Приём гостей
Cafe.guest_arrival()
# Обслуживание гостей
Cafe.discuss_guests()
