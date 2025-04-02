def distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return abs(x2 - x1) + abs(y2 - y1)

def tsp_vizinho_proximo(cidades, inicio):
    visitadas = set([inicio])
    rota = [inicio]
    atual = inicio

    while len(visitadas) < len(cidades):
        min_dist = float('inf')
        proxima_cidade = None
        for cidade in sorted(cidades.keys(), reverse=True):
            if cidade not in visitadas:
                dist = distancia(cidades[atual], cidades[cidade])
                if dist < min_dist:
                    min_dist = dist
                    proxima_cidade = cidade
        if proxima_cidade:
            rota.append(proxima_cidade)
            visitadas.add(proxima_cidade)
            atual = proxima_cidade

    return rota

def main():
    cidades = {
        'A': (0, 0),
        'B': (1, 5),
        'C': (5, 2),
        'D': (6, 6),
        'E': (8, 3)
    }
    inicio = 'A'
    rota = tsp_vizinho_proximo(cidades, inicio)
    print("Rota encontrada:", " -> ".join(rota))

if __name__ == "__main__":
    main()