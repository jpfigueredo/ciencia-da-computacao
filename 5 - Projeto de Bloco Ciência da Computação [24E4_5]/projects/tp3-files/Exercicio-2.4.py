from multiprocessing import Pool, cpu_count
import math
import time

def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def conta_primos_sequencial(inicio, fim):
    return sum(1 for i in range(inicio, fim) if eh_primo(i))

def conta_primos_paralelo(inicio, fim):
    num_processos = cpu_count()
    tamanho_parte = (fim - inicio) // num_processos
    intervalos = [(inicio + i * tamanho_parte, inicio + (i + 1) * tamanho_parte) for i in range(num_processos)]

    with Pool(processes=num_processos) as pool:
        contagens = pool.map(lambda intervalo: conta_primos_sequencial(*intervalo), intervalos)

    return sum(contagens)

if __name__ == '__main__':
    inicio, fim = 1, 100_001

    # Execução sequencial
    start_time = time.time()
    total_primos_sequencial = conta_primos_sequencial(inicio, fim)
    tempo_sequencial = time.time() - start_time
    print(f'Sequencial: {total_primos_sequencial} primos encontrados em {tempo_sequencial:.2f} segundos.')

    # Execução paralela
    start_time = time.time()
    total_pr
::contentReference[oaicite:0]{index=0}

