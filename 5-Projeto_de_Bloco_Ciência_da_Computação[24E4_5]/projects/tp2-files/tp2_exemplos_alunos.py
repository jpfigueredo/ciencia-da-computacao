# Grupo 1 - Processos Assíncronos e Paralelos

# Exercício 1.1: Download Assíncrono de URLs
import asyncio
import aiohttp

async def download_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Downloaded {url}: {len(content)} bytes")

async def main():
    urls = ["https://example.com", "https://httpbin.org/get", "https://jsonplaceholder.typicode.com/posts"]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(download_url(session, url) for url in urls))

# asyncio.run(main())

# Exercício 1.2: Cálculo Paralelo com OpenMP (simulação com multiprocessing)
from multiprocessing import Pool
import random

def sum_chunk(chunk):
    return sum(chunk)

data = [random.randint(1, 100000) for _ in range(10000)]
chunks = [data[i:i + 1000] for i in range(0, len(data), 1000)]

with Pool() as pool:
    result = sum(pool.map(sum_chunk, chunks))
print(f"Soma total: {result}")

# Exercício 1.3: Processamento de Imagens Assíncrono
from PIL import Image, ImageFilter
import os

async def process_image(image_path, output_dir):
    img = Image.open(image_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(os.path.join(output_dir, os.path.basename(image_path)))

async def main_image_processing():
    input_dir = "input_images"
    output_dir = "output_images"
    os.makedirs(output_dir, exist_ok=True)
    images = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]

    await asyncio.gather(*(process_image(img, output_dir) for img in images))

# asyncio.run(main_image_processing())



# Grupo 5 - Computação Paralela em Estruturas de Dados Complexas

# Exercício 5.1: Soma de Elementos em uma Lista
from multiprocessing import Pool

def sum_parallel(lst):
    with Pool() as pool:
        chunk_size = len(lst) // 4
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        results = pool.map(sum, chunks)
    return sum(results)

large_list = list(range(1, 10001))
print(f"Soma paralela: {sum_parallel(large_list)}")

# Exercício 5.2: Busca em Árvore Binária
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parallel_search(root, target):
    from multiprocessing import Process, Value

    def search_subtree(node, target, found):
        if node is None or found.value:
            return
        if node.value == target:
            found.value = True
            return
        search_subtree(node.left, target, found)
        search_subtree(node.right, target, found)

    found = Value('b', False)
    left_proc = Process(target=search_subtree, args=(root.left, target, found))
    right_proc = Process(target=search_subtree, args=(root.right, target, found))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()

    return found.value

# Construção da árvore
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

print(f"Valor encontrado: {parallel_search(root, 7)}")

# Grupo 6 - Programação Dinâmica

# Exercício 6.1: Problema da Mochila
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(f"Valor máximo da mochila: {knapsack(values, weights, capacity)}")

# Exercício 6.2: Sequência Longa Comum (LCS)
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print(f"Comprimento da LCS: {lcs(X, Y)}")

