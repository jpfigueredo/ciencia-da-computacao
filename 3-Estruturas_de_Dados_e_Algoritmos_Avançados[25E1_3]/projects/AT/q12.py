import math
import random
import time

def distance(city1, city2):
    """Calcula a distância euclidiana entre duas cidades."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tsp(cities):
    """Implementa o algoritmo do vizinho mais próximo para o TSP.
    
    Argumentos:
      cities: lista de tuplas (x, y) representando as coordenadas das cidades.
    
    Retorna:
      rota: lista com a ordem de visitação das cidades.
      custo: custo total da rota (distância total).
    """
    N = len(cities)
    if N == 0:
        return [], 0
    
    visitado = [False] * N
    rota = [0]  # Começa pela cidade 0 (ou pode ser escolhida aleatoriamente)
    visitado[0] = True
    custo_total = 0

    atual = 0
    for _ in range(N - 1):
        melhor_vizinho = None
        melhor_dist = float('inf')
        for j in range(N):
            if not visitado[j]:
                d = distance(cities[atual], cities[j])
                if d < melhor_dist:
                    melhor_dist = d
                    melhor_vizinho = j
        rota.append(melhor_vizinho)
        visitado[melhor_vizinho] = True
        custo_total += melhor_dist
        atual = melhor_vizinho

    custo_total += distance(cities[atual], cities[rota[0]])
    rota.append(rota[0])
    return rota, custo_total

if __name__ == "__main__":
    def gerar_cidades(num_cidades, limite=100):
        return [(random.uniform(0, limite), random.uniform(0, limite)) for _ in range(num_cidades)]
    
    tamanhos = [10, 20, 50]  # Número de cidades a testar
    
    for n in tamanhos:
        cidades = gerar_cidades(n)
        print(f"\nTestando TSP com {n} cidades:")
        inicio = time.time()
        rota, custo = nearest_neighbor_tsp(cidades)
        fim = time.time()
        print(f"Rota: {rota}")
        print(f"Custo total: {custo:.2f}")
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
