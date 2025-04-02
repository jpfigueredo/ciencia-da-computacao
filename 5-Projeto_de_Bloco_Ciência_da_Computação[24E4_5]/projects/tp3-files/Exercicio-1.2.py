class NoBST:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(no, valor):
    """Insere um valor na BST."""
    if no is None:
        return NoBST(valor)
    if valor < no.valor:
        no.esquerda = inserir(no.esquerda, valor)
    else:
        no.direita = inserir(no.direita, valor)
    return no

def encontrar_minimo(no):
    """Encontra o nó com o menor valor na BST."""
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

def remover(no, valor):
    """Remove um valor da BST e retorna a nova raiz."""
    if no is None:
        return no

    # Se o valor a ser removido é menor, está na subárvore esquerda
    if valor < no.valor:
        no.esquerda = remover(no.esquerda, valor)
    # Se o valor a ser removido é maior, está na subárvore direita
    elif valor > no.valor:
        no.direita = remover(no.direita, valor)
    # Valor encontrado
    else:
        # Caso 1: Nó sem filhos (nó folha)
        if no.esquerda is None and no.direita is None:
            return None
        # Caso 2: Nó com apenas um filho
        elif no.esquerda is None:
            return no.direita
        elif no.direita is None:
            return no.esquerda
        # Caso 3: Nó com dois filhos
        else:
            # Encontra o sucessor in-order (menor na subárvore direita)
            sucessor = encontrar_minimo(no.direita)
            # Substitui o valor do nó pelo valor do sucessor
            no.valor = sucessor.valor
            # Remove o sucessor in-order
            no.direita = remover(no.direita, sucessor.valor)

    return no

def percurso_in_order(no):
    """Realiza o percurso in-order na BST e retorna uma lista de valores."""
    return (percurso_in_order(no.esquerda) +
            [no.valor] +
            percurso_in_order(no.direita)) if no else []

# Exemplo de uso:
# Construindo a árvore com os elementos [50, 30, 70, 20, 40, 60, 80]
raiz = None
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    raiz = inserir(raiz, elem)

print("Percurso in-order antes das remoções:", percurso_in_order(raiz))

# Removendo os nós 20, 30 e 50
for valor in [20, 30, 50]:
    raiz = remover(raiz, valor)
    print(f"Percurso in-order após remover {valor}:", percurso_in_order(raiz))
