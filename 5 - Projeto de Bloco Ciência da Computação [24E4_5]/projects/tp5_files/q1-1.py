import heapq

def dijkstra(grafo, origem):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[origem] = 0

    fila = [(0, origem)]
    heapq.heapify(fila)
    visitados = set()

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)

        for vizinho, peso in grafo[vertice_atual]:
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))

    return distancias

def main():
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    origem = 'A'
    distancias = dijkstra(grafo, origem)

    print(f"Distâncias mínimas a partir de {origem}:")
    for vertice, distancia in distancias.items():
        print(f"Ilha {vertice}: {distancia} dias de navegação")

if __name__ == "__main__":
    main()
