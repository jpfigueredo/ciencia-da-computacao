import time

def ler_arquivos(caminho):
    with open(caminho, 'r') as f:
        return f.read().splitlines()

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

def medir_tempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista.copy())
    return time.time() - inicio

if __name__ == "__main__":
    arquivos = ler_arquivos('listagem_arquivos.txt')
    tempos = {
        'Bubble Sort': medir_tempo(bubble_sort, arquivos),
        'Selection Sort': medir_tempo(selection_sort, arquivos),
        'Insertion Sort': medir_tempo(insertion_sort, arquivos)
    }
    for nome, tempo in tempos.items():
        print(f"{nome}: {tempo:.5f} segundos")
