def escalonar_tarefas(tarefas, dependencias, num_maquinas):  
    ordem = []  
    visitados = set()  

    def dfs(tarefa):  
        if tarefa not in visitados:  
            visitados.add(tarefa)  
            for dep in dependencias.get(tarefa, []):  
                dfs(dep)  
            ordem.append(tarefa)  

    for t in tarefas:  
        dfs(t)  
    ordem = reversed(ordem)  

    maquinas = [0] * num_maquinas  
    conclusao = {t: 0 for t in tarefas}  

    for t in ordem:  
        inicio = max([conclusao[dep] for dep in dependencias.get(t, [])] + [0])  
        maq = maquinas.index(min(maquinas))  
        fim = max(inicio, maquinas[maq]) + tarefas[t]  
        conclusao[t] = fim  
        maquinas[maq] = fim  

    return max(maquinas)  

tarefas = {'T1': 5, 'T2': 3, 'T3': 2}  
dependencias = {'T3': ['T1']}
num_maquinas = 2  

makespan = escalonar_tarefas(tarefas, dependencias, num_maquinas)  
print(f"Tempo total mínimo: {makespan} minutos")