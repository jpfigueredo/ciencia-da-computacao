def mochila_gulosa(itens, capacidade):
    itens_ordenados = sorted(itens, key=lambda x: x[2]/x[1], reverse=True)
    
    mochila = []
    peso_total = 0
    valor_total = 0
    
    for item in itens_ordenados:
        nome, peso, valor = item
        if peso_total + peso <= capacidade:
            mochila.append(nome)
            peso_total += peso
            valor_total += valor
    
    return mochila, valor_total, peso_total

itens = [
    ('item1', 2, 40),
    ('item2', 3, 50),
    ('item3', 5, 100),
    ('item4', 4, 90)
]
capacidade = 8

mochila, valor, peso = mochila_gulosa(itens, capacidade)
print("Itens selecionados:", mochila)
print("Valor total:", valor)
print("Peso total:", peso)


