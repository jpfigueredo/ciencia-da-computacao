import heapq

def prim_mst(grafo, inicio):
    visitados = set([inicio])
    arestas_mst = []
    fila = []
    
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila, (peso, inicio, vizinho))
    
    while fila:
        peso, u, v = heapq.heappop(fila)

        if v in visitados:
            continue
        
        visitados.add(v)
        arestas_mst.append((u, v, peso))
        
        for vizinho, peso_viz in grafo[v]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso_viz, v, vizinho))

    return arestas_mst

def main():
    grafo = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]
    }

    inicio = 'A'
    mst = prim_mst(grafo, inicio)

    print(f"Árvore Geradora Mínima a partir de {inicio}:")
    for u, v, peso in mst:
        print(f"{u} - {v} com peso {peso}")

if __name__ == "__main__":
    main()