from concurrent.futures import ThreadPoolExecutor

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def dfs_paralela(no, valor, caminho):
    if no is None:
        return None
    caminho.append(no.valor)
    if no.valor == valor:
        return caminho.copy()
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(dfs_paralela, no.esquerda, valor, caminho),
                   executor.submit(dfs_paralela, no.direita, valor, caminho)]
        for futuro in futuros:
            resultado = futuro.result()
            if resultado:
                return resultado
    caminho.pop()
    return None

# Exemplo de uso
if __name__ == '__main__':
    # Construindo a árvore binária
    raiz = No(1)
    raiz.esquerda = No(2)
    raiz.direita = No(3)
    raiz.esquerda.esquerda = No(4)
    raiz.esquerda.direita = No(5)
    raiz.direita.esquerda = No(6)
    raiz.direita.direita = No(7)
    
    # Buscando o caminho até o nó 5
    valor_buscado = 5
    caminho = []
    resultado = dfs_paralela(raiz, valor_buscado, caminho)
    if resultado:
        print(f'O caminho até o valor {valor_buscado} é: {resultado}')
    else:
        print(f'O valor {valor_buscado} não foi encontrado na árvore.')

