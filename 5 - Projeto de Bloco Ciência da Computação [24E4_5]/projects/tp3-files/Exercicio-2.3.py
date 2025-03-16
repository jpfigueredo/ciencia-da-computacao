from multiprocessing import Pool, cpu_count
import math

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

def conta_primos(intervalo):
    inicio, fim = intervalo
    return sum(1 for i in range(inicio, fim) if eh_primo(i))

if __name__ == '__main__':
    intervalo_total = (1, 100_001)
    num_processos = cpu_count()
    tamanho_parte = (intervalo_total[1] - intervalo_total[0]) // num_processos
    intervalos = [(i * tamanho_parte + 1, (i + 1) * tamanho_parte + 1) for i in range(num_processos)]
    
    with Pool(processes=num_processos) as pool:
        contagens = pool.map(conta_primos, intervalos)
    
    total_primos = sum(contagens)
    print(f'Número total de primos entre {intervalo_total[0]} e {intervalo_total[1] - 1}: {total_primos}')

