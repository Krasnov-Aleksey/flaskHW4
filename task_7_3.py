"""Многопроцессорность"""
import multiprocessing
from random import randint
import time

arr = []
pars_elements = []
sum_el = multiprocessing.Value('i', 0)


def fill_arr(amount):
    for _ in range(amount):
        arr.append(randint(1, 101))


def shear_element(sh):
    step = int(len(arr) / sh)
    for i in range(0, len(arr), step):
        pars_elements.append(arr[i:i + step])


def sum_arr(item, sum_el):
    # global sum_el
    with sum_el.get_lock():
        sum_el.value = sum_el.value + sum(item)


if __name__ == '__main__':
    fill_arr(1_000_000)
    shear_element(5)
    start_time = time.time()
    processes = []
    for items in pars_elements:
        process = multiprocessing.Process(target=sum_arr, args=(items, sum_el))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    print(f'Сумма элементов {sum_el.value:_} время выполнения {time.time() - start_time:.4f}')
