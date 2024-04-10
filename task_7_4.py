"""Асинхронность"""

from random import randint
import time
import asyncio

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


async def sum_arr(item):
    global sum_el
    sum_el = sum_el + sum(item)


async def main():
    tasks = []
    for items in pars_elements:
        task = asyncio.ensure_future(sum_arr(items))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    fill_arr(1_000_000)
    shear_element(5)
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Сумма элементов {sum_el:_} время выполнения {time.time() - start_time:.4f}')

