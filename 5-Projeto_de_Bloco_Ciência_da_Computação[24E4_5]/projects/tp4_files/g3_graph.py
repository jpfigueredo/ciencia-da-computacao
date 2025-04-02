from collections import deque

def construir_grafo(arestas, direcionado=False):
    grafo = {}
    for u, v in arestas:
        if u not in grafo:
            grafo[u] = []
        grafo[u].append(v)
        if not direcionado:
            if v not in grafo:
                grafo[v] = []
            grafo[v].append(u)
    return grafo

def exibir_grafo(grafo):
    for vertice, adjacentes in grafo.items():
        print(f"{vertice}: {', '.join(adjacentes)}")

def dfs(grafo, inicio):
    visitados = set()
    ordem = []
    
    def _dfs_recursiva(no):
        if no not in visitados:
            visitados.add(no)
            ordem.append(no)
            for vizinho in grafo.get(no, []):
                _dfs_recursiva(vizinho)
    
    _dfs_recursiva(inicio)
    return ordem

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    ordem = []
    
    visitados.add(inicio)
    
    while fila:
        no = fila.popleft()
        ordem.append(no)
        for vizinho in grafo.get(no, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    
    return ordem

def encontrar_caminho(grafo, inicio, fim):
    if inicio not in grafo or fim not in grafo:
        return None
    fila = deque([inicio])
    pais = {inicio: None}
    while fila:
        no_atual = fila.popleft()
        if no_atual == fim:
            break
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in pais:
                pais[vizinho] = no_atual
                fila.append(vizinho)
    if fim not in pais:
        return None
    caminho = []
    no = fim
    while no is not None:
        caminho.append(no)
        no = pais[no]
    caminho.reverse()
    return caminho


if __name__ == "__main__":
    arestas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    print("=== Grafo Não Orientado ===")
    grafo_nao_orientado = construir_grafo(arestas)
    exibir_grafo(grafo_nao_orientado)
    print("DFS a partir de A:", dfs(grafo_nao_orientado, 'A'))  
    print("BFS a partir de A:", bfs(grafo_nao_orientado, 'A'))  
    print("Caminho de A para E:", encontrar_caminho(grafo_nao_orientado, 'A', 'E'))  