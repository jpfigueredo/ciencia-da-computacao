def greedy_set_cover(lojas, armazens):  
    cobertas = set()  
    solucao = []  

    while len(cobertas) < len(lojas):  
        melhor_armazem = None  
        max_cobertura = 0  

        for armazem in armazens:  
            cobertura = len(armazem['lojas'] - cobertas)  
            if cobertura > max_cobertura:  
                max_cobertura = cobertura  
                melhor_armazem = armazem  

        if melhor_armazem is None:  
            break

        solucao.append(melhor_armazem)  
        cobertas.update(melhor_armazem['lojas'])  

    return solucao  

lojas = {'L1', 'L2', 'L3', 'L4', 'L5'}  
armazens = [  
    {'id': 'A1', 'lojas': {'L1', 'L2', 'L3'}},  
    {'id': 'A2', 'lojas': {'L3', 'L4'}},  
    {'id': 'A3', 'lojas': {'L4', 'L5'}}  
]  

solucao = greedy_set_cover(lojas, armazens)  
print([armazem['id'] for armazem in solucao])
