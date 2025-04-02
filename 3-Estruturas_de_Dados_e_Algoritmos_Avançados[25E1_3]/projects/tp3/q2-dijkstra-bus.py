import heapq

def encontrar_menor_caminho(grafo, inicio, fim):
    distancias = {no: float('inf') for no in grafo}
    predecessores = {no: None for no in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if no_atual == fim:
            break
            
        if distancia_atual > distancias[no_atual]:
            continue
            
        for vizinho, peso in grafo[no_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
    
    caminho = []
    no_atual = fim
    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = predecessores[no_atual]
    caminho.reverse()
    
    if not caminho or caminho[0] != inicio:
        return None, None
    
    return caminho, distancias[fim]

grafo_cidade = {
    'Centro': [('Bela Vista', 5), ('Liberdade', 2)],
    'Bela Vista': [('Centro', 5), ('Moema', 3), ('Pinheiros', 6)],
    'Liberdade': [('Centro', 2), ('Moema', 1)],
    'Moema': [('Bela Vista', 3), ('Liberdade', 1), ('Pinheiros', 4)],
    'Pinheiros': [('Bela Vista', 6), ('Moema', 4)]
}

inicio = 'Centro'
fim = 'Pinheiros'
caminho, tempo_total = encontrar_menor_caminho(grafo_cidade, inicio, fim)

print(f"🔄 Análise de Rota: {inicio} → {fim}")
print("═" * 40)
print(f"🏁 Caminho mais rápido: {' → '.join(caminho)}")
print(f"⏱️  Tempo total estimado: {tempo_total} minutos")
print("═" * 40)
print("🗺️  Detalhes do Percurso:")
for i in range(len(caminho)-1):
    origem = caminho[i]
    destino = caminho[i+1]
    peso = next(p for v, p in grafo_cidade[origem] if v == destino)
    print(f"  • {origem} → {destino} ({peso} minutos)")