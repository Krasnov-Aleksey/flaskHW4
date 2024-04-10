"""
Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.
"""

from random import randint
import time

arr = []


def fill_arr(amount):
    for i in range(amount):
        arr.append(randint(1, 101))


def sum_elem_arr():
    res = sum(arr)
    return res


if __name__ == '__main__':
    fill_arr(1_000_000)
    start_time = time.time()
    print(f'Сумма элементов {sum_elem_arr():_} время выполнения {time.time() - start_time:.4f}')
