metro_grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E']
}


def dfs(grafo, inicio):
    visitados = set()
    pilha = [inicio]

    while pilha:
        vertice = pilha.pop()
        if vertice not in visitados:
            print(vertice, end=' ')
            visitados.add(vertice)
            for vizinho in sorted(grafo[vertice], reverse=True):
                if vizinho not in visitados:
                    pilha.append(vizinho)


from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            print(vertice, end=' ')
            visitados.add(vertice)
            for vizinho in sorted(grafo[vertice]):
                if vizinho not in visitados:
                    fila.append(vizinho)
