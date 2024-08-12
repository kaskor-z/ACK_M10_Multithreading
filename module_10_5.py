
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
    print(f' Количество строк в списке: {len(all_data)}')


# ЛИНЕНЫЙ вызов кода
Files = [f'./Files/file {namber}.txt' for namber in range(1, 5)]
time_start = datetime.now()
for file_name in Files: read_info(file_name)
time_end = datetime.now()
long_time_ = time_end - time_start
print(f'Время выполнения линейного вызова кода: {long_time_}')

# МНОГОПРОЦЕССНЫЙ вызов кода
if __name__ == '__main__':
    print(f'---------------------------------')
    Files = [f'./Files/file {namber}.txt' for namber in range(1, 5)]
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, Files)
    time_end = datetime.now()
    long_time_ = time_end - time_start
    print(f'Время выполнения многопроцессный  вызова кода: {long_time_}')
