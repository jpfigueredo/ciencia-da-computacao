from concurrent.futures import ThreadPoolExecutor

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontra_maximo_paralelo(no):
    if no is None:
        return float('-inf')
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(encontra_maximo_paralelo, no.esquerda),
                   executor.submit(encontra_maximo_paralelo, no.direita)]
        max_esquerda = futuros[0].result()
        max_direita = futuros[1].result()
    return max(no.valor, max_esquerda, max_direita)

# Exemplo de uso
if __name__ == '__main__':
    # Construindo a árvore binária
    raiz = No(15)
    raiz.esquerda = No(10)
    raiz.direita = No(20)
    raiz.esquerda.esquerda = No(8)
    raiz.esquerda.direita = No(12)
    raiz.direita.esquerda = No(17)
    raiz.direita.direita = No(25)
    
    # Encontrando o valor máximo
    max_valor = encontra_maximo_paralelo(raiz)
    print(f'O valor máximo na árvore é: {max_valor}')

