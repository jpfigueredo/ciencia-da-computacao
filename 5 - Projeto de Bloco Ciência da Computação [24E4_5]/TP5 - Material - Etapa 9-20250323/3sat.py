import random
import itertools
import sys
import time
import matplotlib.pyplot as plt

def gera_instancia_3sat(num_clausulas, num_variaveis):
    """
    Gera uma instância aleatória de 3SAT.
    Cada cláusula contém 3 literais escolhidos aleatoriamente dentre as variáveis,
    garantindo que cada cláusula possua 3 variáveis distintas. Cada literal pode ser
    negado com probabilidade 50%.
    """
    formula = []
    for _ in range(num_clausulas):
        # Seleciona 3 variáveis distintas
        variaveis = random.sample(range(1, num_variaveis + 1), 3)
        clausula = []
        for v in variaveis:
            # Cada literal é v ou -v, escolhido aleatoriamente
            literal = v if random.choice([True, False]) else -v
            clausula.append(literal)
        formula.append(clausula)
    return formula

def verifica_satisfacao(formula, atribuicao):
    """
    Verifica se a fórmula (lista de cláusulas) é satisfeita pela atribuição fornecida.
    'atribuicao' é um dicionário que mapeia cada variável (1 até num_variaveis)
    para um valor booleano (True/False).
    """
    for clausula in formula:
        satisfazida = False
        for literal in clausula:
            if literal > 0 and atribuicao[abs(literal)]:
                satisfazida = True
                break
            elif literal < 0 and not atribuicao[abs(literal)]:
                satisfazida = True
                break
        if not satisfazida:
            return False
    return True

def resolve_3sat(formula, num_variaveis):
    """
    Resolve a instância 3SAT usando busca por força bruta.
    Testa todas as possíveis atribuições de valores às variáveis.
    Retorna uma atribuição que satisfaz a fórmula, ou None se não houver solução.
    """
    for valores in itertools.product([False, True], repeat=num_variaveis):
        atribuicao = {i+1: valor for i, valor in enumerate(valores)}
        if verifica_satisfacao(formula, atribuicao):
            return atribuicao
    return None

def executar_instancia(num_clausulas):
    """
    Gera e resolve uma instância de 3SAT com 'num_clausulas'.
    O número de variáveis é definido como o máximo entre 3 e num_clausulas.
    Retorna uma tupla: (tempo_de_execucao, satisfatibilidade, formula, solucao)
    """
    num_variaveis = max(3, num_clausulas)
    formula = gera_instancia_3sat(num_clausulas, num_variaveis)
    
    inicio = time.perf_counter()
    solucao = resolve_3sat(formula, num_variaveis)
    fim = time.perf_counter()
    
    tempo_execucao = fim - inicio
    satisfatibilidade = solucao is not None
    
    return tempo_execucao, satisfatibilidade, formula, solucao

def imprimir_tabela(resultados):
    """
    Exibe uma tabela com o número de cláusulas, tempo de execução e se a instância foi satisfatível.
    """
    print(f"\n{'Cláusulas':>10} | {'Tempo (s)':>10} | {'Satisfatível':>13}")
    print("-" * 40)
    for num_clausulas, tempo, sat in resultados:
        print(f"{num_clausulas:>10} | {tempo:10.4f} | {str(sat):>13}")

def plotar_grafico(resultados):
    """
    Plota um gráfico de linha com o tempo de execução para cada tamanho de instância.
    """
    clausulas = [r[0] for r in resultados]
    tempos = [r[1] for r in resultados]
    
    plt.figure()
    plt.plot(clausulas, tempos, marker='o', linestyle='-')
    plt.xlabel("Número de Cláusulas")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Desempenho do Algoritmo 3SAT")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Se o usuário fornecer 1 parâmetro (além do nome do script), executa para uma única instância.
    # Se fornecer 2 parâmetros, executa para um intervalo de cláusulas.
    if len(sys.argv) not in [2, 3]:
        print("Uso:")
        print("  Modo único: python script.py <num_clausulas>")
        print("  Modo intervalo: python script.py <min_clausulas> <max_clausulas>")
        return

    # Modo único
    if len(sys.argv) == 2:
        try:
            num_clausulas = int(sys.argv[1])
        except ValueError:
            print("O parâmetro deve ser um número inteiro.")
            return

        tempo, sat, formula, solucao = executar_instancia(num_clausulas)
        print("Instância 3SAT gerada (forma CNF):")
        for clausula in formula:
            print(clausula)
        print(f"\nTempo de execução: {tempo:.4f} segundos")
        if sat:
            print("Instância SATISFATÍVEL!")
            print("Uma atribuição que satisfaz a instância:")
            print(solucao)
        else:
            print("Instância NÃO SATISFATÍVEL.")

    # Modo intervalo
    else:
        try:
            min_clausulas = int(sys.argv[1])
            max_clausulas = int(sys.argv[2])
        except ValueError:
            print("Os parâmetros devem ser números inteiros.")
            return

        if min_clausulas > max_clausulas:
            print("O número mínimo de cláusulas deve ser menor ou igual ao número máximo.")
            return

        resultados = []  # Lista de tuplas: (num_clausulas, tempo, satisfatibilidade)
        for num in range(min_clausulas, max_clausulas + 1):
            print(f"Executando instância com {num} cláusulas...")
            tempo, sat, _, _ = executar_instancia(num)
            resultados.append((num, tempo, sat))

        # Exibe a tabela com os resultados
        imprimir_tabela(resultados)
        # Plota o gráfico de tempo de execução
        plotar_grafico(resultados)

if __name__ == "__main__":
    main()