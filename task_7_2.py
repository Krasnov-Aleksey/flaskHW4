"""Многопоточность"""

from random import randint
import time
import threading

arr = []
pars_elements = []
sum_el = 0


def fill_arr(amount):
    for _ in range(amount):
        arr.append(randint(1, 101))


def shear_element(sh):
    step = int(len(arr) / sh)
    for i in range(0, len(arr), step):
        pars_elements.append(arr[i:i + step])


def sum_arr(item):
    global sum_el
    sum_el = sum_el + sum(item)


if __name__ == '__main__':
    fill_arr(1_000_000)
    shear_element(5)
    start_time = time.time()
    threads = []
    for items in pars_elements:
        thread = threading.Thread(target=sum_arr, args=[items])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print(f'Сумма элементов {sum_el:_} время выполнения {time.time() - start_time:.4f}')
