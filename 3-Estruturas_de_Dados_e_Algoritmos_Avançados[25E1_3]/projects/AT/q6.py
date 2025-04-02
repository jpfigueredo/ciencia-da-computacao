grafo = {
    'CD': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'A': 3, 'D': 8},
    'C': {'E': 4, 'D': 2},
    'D': {'E': 6, 'F': 5},
    'E': {'F': 3},
    'F': {'C': 1, 'E': 1}
}


import heapq

def dijkstra(grafo, inicio, fim):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    caminho = {}

    while fila_prioridade:
        distancia_atual, nodo_atual = heapq.heappop(fila_prioridade)

        if nodo_atual == fim:
            break

        for vizinho, peso in grafo[nodo_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
                caminho[vizinho] = nodo_atual

    caminho_otimo = []
    passo = fim
    while passo in caminho:
        caminho_otimo.insert(0, passo)
        passo = caminho[passo]
    caminho_otimo.insert(0, inicio)

    return caminho_otimo, distancias[fim]

inicio = 'CD'
fim = 'F'
rota, custo = dijkstra(grafo, inicio, fim)
print(f"Rota ótima: {' -> '.join(rota)} com distância total de {custo} km")
