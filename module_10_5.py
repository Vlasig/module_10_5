import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":
    start1 = datetime.datetime.now()
    for i in filenames:
        read_info(i)
    end1 = datetime.datetime.now()
    print('Линейный алгоритм: ', end1 - start1)  # 0:00:08.376193

    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end2 = datetime.datetime.now()
    print('Многопроцессный алгоритм: ', end2 - start2)  # 0:00:02.959001
