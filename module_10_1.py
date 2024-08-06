from datetime import datetime
from time import sleep
from threading import Thread

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}" + '\n' )
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start_func = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end_func = datetime.now()
time_res_func = time_end_func - time_start_func
print(f' === Интервал времени работы функции "Запись в файл" = {time_res_func}')

time_start_thread = datetime.now()
print(f'Работа потоков началась: {time_start_thread}')

write_word_thread_5 = Thread(target=wite_words, args=(10, 'example5.txt'))
write_word_thread_6 = Thread(target=wite_words, args=(30, 'example6.txt'))
write_word_thread_7 = Thread(target=wite_words, args=(200, 'example7.txt'))
write_word_thread_8 = Thread(target=wite_words, args=(100, 'example8.txt'))

write_word_thread_5.start()
write_word_thread_6.start()
write_word_thread_7.start()
write_word_thread_8.start()

write_word_thread_5.join()
write_word_thread_6.join()
write_word_thread_7.join()
write_word_thread_8.join()

time_end_thread = datetime.now()
print(f'Работа потоков закончилась: {time_end_thread}')
time_res_thread = time_end_thread - time_start_thread
print(f' === Интервал времени работы потоков с функцией "Запись в файл" = {time_res_thread}')







