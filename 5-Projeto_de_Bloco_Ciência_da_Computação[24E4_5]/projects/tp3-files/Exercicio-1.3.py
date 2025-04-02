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

def buscar(no, valor):
    """Busca um valor na BST. Retorna True se encontrado, caso contrário, False."""
    if no is None:
        return False
    if valor == no.valor:
        return True
    elif valor < no.valor:
        return buscar(no.esquerda, valor)
    else:
        return buscar(no.direita, valor)

# Exemplo de uso:
# Criando a árvore e inserindo elementos
raiz = None
elementos = [50, 30, 20, 40, 70, 60, 80]
for elem in elementos:
    raiz = inserir(raiz, elem)

# Buscando o valor 40
valor_procurado = 40
if buscar(raiz, valor_procurado):
    print(f"Valor {valor_procurado} encontrado na BST.")
else:
    print(f"Valor {valor_procurado} não encontrado na BST.")
