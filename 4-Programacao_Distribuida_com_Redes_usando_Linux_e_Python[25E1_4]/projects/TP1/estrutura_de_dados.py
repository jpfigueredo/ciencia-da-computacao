import time
from collections import deque
import hashlib

class HashTable:
    def __init__(self):
        self.table = {}

    def inserir(self, chave, valor):
        hash_chave = hashlib.md5(chave.encode()).hexdigest()
        self.table[hash_chave] = valor

    def buscar(self, chave):
        hash_chave = hashlib.md5(chave.encode()).hexdigest()
        return self.table.get(hash_chave)

    def remover(self, chave):
        hash_chave = hashlib.md5(chave.encode()).hexdigest()
        return self.table.pop(hash_chave, None)


def ler_arquivos(caminho):
    with open(caminho, 'r') as f:
        return f.read().splitlines()

def medir_tempo_execucao(funcao, *args):
    inicio = time.time()
    resultado = funcao(*args)
    return resultado, time.time() - inicio

if __name__ == "__main__":
    arquivos = ler_arquivos('listagem_arquivos.txt')
    pilha = arquivos.copy()
    fila = deque(arquivos)
    tabela_hash = HashTable()

    for arquivo in arquivos:
        tabela_hash.inserir(arquivo, arquivo)

    # Recuperar posições especificadas
    posicoes = [0, 99, 999, 4999, len(arquivos) - 1]
    print("Posições na Pilha:", [pilha[pos] for pos in posicoes])
    print("Posições na Fila:", [fila[pos] for pos in posicoes])
    print("Posições na Tabela Hash:", [tabela_hash.buscar(arquivos[pos]) for pos in posicoes])