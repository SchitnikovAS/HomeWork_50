from time import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time()
    for name in filenames:
        read_info(name)
    end_time = time()
    print(f'Время выполнения при линейном подходе: {end_time - start_time}')

    start_time = time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time()
    print(f'Время выполнения при многопроцессорном подходе: {end_time - start_time}')
