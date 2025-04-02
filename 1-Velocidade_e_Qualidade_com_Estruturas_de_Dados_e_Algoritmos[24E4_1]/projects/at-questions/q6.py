import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

prices_1000 = [random.uniform(1, 1000) for _ in range(1000)]
prices_10000 = [random.uniform(1, 1000) for _ in range(10000)]

start_time = time.time()
bubble_sort(prices_1000)
time_1000 = time.time() - start_time

start_time = time.time()
bubble_sort(prices_10000)
time_10000 = time.time() - start_time

print(f"Tempo para ordenar 1.000 elementos: {time_1000:.2f} segundos")
print(f"Tempo para ordenar 10.000 elementos: {time_10000:.2f} segundos")
