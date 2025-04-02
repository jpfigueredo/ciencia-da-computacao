from concurrent.futures import ThreadPoolExecutor

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def busca_paralela(no, valor):
    if no is None:
        return False
    if no.valor == valor:
        return True
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuros = [executor.submit(busca_paralela, no.esquerda, valor),
                   executor.submit(busca_paralela, no.direita, valor)]
        for futuro in futuros:
            if futuro.result():
                return True
    return False

# Exemplo de uso
if __name__ == '__main__':
    # Construindo a árvore binária
    raiz = No(50)
    raiz.esquerda = No(30)
    raiz.direita = No(70)
    raiz.esquerda.esquerda = No(20)
    raiz.esquerda.direita = No(40)
    raiz.direita.esquerda = No(60)
    raiz.direita.direita = No(80)
    
    # Buscando o valor 60
    valor_buscado = 60
    encontrado = busca_paralela(raiz, valor_buscado)
    if encontrado:
        print(f'O valor {valor_buscado} foi encontrado na árvore.')
    else:
        print(f'O valor {valor_buscado} não foi encontrado na árvore.')

