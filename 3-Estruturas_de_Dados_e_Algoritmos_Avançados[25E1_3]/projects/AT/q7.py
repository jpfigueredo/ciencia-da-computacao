def floyd_warshall(grafo):
    n = len(grafo)
    dist = [linha[:] for linha in grafo]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

INF = float('inf')
grafo = [
    [  0,   5, INF,  10, INF, INF],
    [  5,   0,   3, INF, INF, INF],
    [INF,   3,   0,   1,   7, INF],
    [ 10, INF,   1,   0,   2, INF],
    [INF, INF,   7,   2,   0,   4],
    [INF, INF, INF, INF,   4,   0]
]

matriz_distancias = floyd_warshall(grafo)

print("Matriz de Menores Tempos (minutos):")
bairros = ['A', 'B', 'C', 'D', 'E', 'F']
print("   " + "  ".join(bairros))
for i in range(len(matriz_distancias)):
    linha = [str(x) if x != INF else "∞" for x in matriz_distancias[i]]
    print(f"{bairros[i]}  {'  '.join(linha)}")
