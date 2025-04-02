class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def eh_bst_util(no, minimo, maximo):
    # Uma árvore vazia é considerada uma BST
    if no is None:
        return True

    # Verifica se o valor do nó atual está dentro dos limites permitidos
    if no.valor <= minimo or no.valor >= maximo:
        return False

    # Recursivamente verifica as subárvores esquerda e direita,
    # atualizando os limites
    return (eh_bst_util(no.esquerda, minimo, no.valor) and
            eh_bst_util(no.direita, no.valor, maximo))

def eh_bst(raiz):
    import math
    return eh_bst_util(raiz, -math.inf, math.inf)

# Exemplo de uso:
# Construindo uma árvore binária
raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(2)
raiz.esquerda.direita = No(7)
raiz.direita.esquerda = No(12)
raiz.direita.direita = No(20)

# Verificando se a árvore é uma BST
if eh_bst(raiz):
    print("A árvore é uma BST válida.")
else:
    print("A árvore não é uma BST válida.")

# Alterando manualmente um nó para invalidar a propriedade BST
raiz.direita.esquerda.valor = 8

# Verificando novamente
if eh_bst(raiz):
    print("A árvore é uma BST válida.")
else:
    print("A árvore não é uma BST válida.")
