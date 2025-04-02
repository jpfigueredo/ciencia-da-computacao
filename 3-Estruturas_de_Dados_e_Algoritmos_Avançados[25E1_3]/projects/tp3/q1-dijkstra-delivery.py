import heapq

def dijkstra(grafo, origem):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        if distancia_atual > distancias[vertice_atual]:
            continue
            
        for vizinho, peso in grafo[vertice_atual]:
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias

grafo_logistica = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

centro_distribuicao = 'A'
resultado = dijkstra(grafo_logistica, centro_distribuicao)

print(f"Menores distâncias a partir de {centro_distribuicao}:")
for bairro, distancia in resultado.items():
    print(f"{bairro}: {distancia} km")