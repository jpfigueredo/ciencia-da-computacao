from multiprocessing import Pool

def multiplica_linha(args):
    A, B, linha = args
    num_colunas_B = len(B[0])
    num_colunas_A = len(A[0])
    resultado_linha = []
    for j in range(num_colunas_B):
        soma = sum(A[linha][k] * B[k][j] for k in range(num_colunas_A))
        resultado_linha.append(soma)
    return resultado_linha

if __name__ == '__main__':
    # Matrizes de exemplo 3x3
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    num_linhas_A = len(A)
    
    # Cria um pool de processos
    with Pool() as pool:
        # Multiplica cada linha em paralelo
        resultado = pool.map(multiplica_linha, [(A, B, i) for i in range(num_linhas_A)])
    
    # Exibe a matriz resultante
    print("Matriz Resultante:")
    for linha in resultado:
        print(linha)

