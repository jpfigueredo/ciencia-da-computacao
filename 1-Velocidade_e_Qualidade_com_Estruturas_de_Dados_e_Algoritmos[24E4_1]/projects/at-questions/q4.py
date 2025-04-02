import random
import time

def gerar_lista_livros():
    return sorted(random.randint(1000000000, 9999999999) for _ in range(100000))

def busca_binaria(isbn, livros):
    inicio = 0
    fim = len(livros) - 1
    iteracoes = 0
    
    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if livros[meio] == isbn:
            return meio, iteracoes
        elif livros[meio] < isbn:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, iteracoes

def busca_linear(isbn, livros):
    iteracoes = 0
    for i, livro in enumerate(livros):
        iteracoes += 1
        if livro == isbn:
            return i, iteracoes
    return -1, iteracoes

if __name__ == "__main__":
    livros = gerar_lista_livros()
    isbn_busca = random.choice(livros)

    print(f"ISBN a ser buscado: {isbn_busca}")

    inicio_tempo_binaria = time.time()
    resultado_binaria, iteracoes_binaria = busca_binaria(isbn_busca, livros)
    tempo_binaria = time.time() - inicio_tempo_binaria
    print(f"Busca binária: Índice encontrado: {resultado_binaria}, Iterações: {iteracoes_binaria}, Tempo: {tempo_binaria:.6f} segundos")

    inicio_tempo_linear = time.time()
    resultado_linear, iteracoes_linear = busca_linear(isbn_busca, livros)
    tempo_linear = time.time() - inicio_tempo_linear
    print(f"Busca linear: Índice encontrado: {resultado_linear}, Iterações: {iteracoes_linear}, Tempo: {tempo_linear:.6f} segundos")
