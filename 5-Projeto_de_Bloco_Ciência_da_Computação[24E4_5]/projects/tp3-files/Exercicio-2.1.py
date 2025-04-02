import concurrent.futures

def soma_parcial(numeros):
    """Calcula a soma de uma sublista de números."""
    return sum(numeros)

if __name__ == "__main__":
    # Cria uma lista de números de 1 até 10 milhões
    numeros = list(range(1, 10_000_001))

    # Define o número de partes para dividir a lista
    num_partes = 10  # Você pode ajustar esse valor conforme necessário

    # Calcula o tamanho de cada parte
    tamanho_parte = len(numeros) // num_partes

    # Cria as sublistas
    sublistas = [numeros[i * tamanho_parte:(i + 1) * tamanho_parte] for i in range(num_partes)]

    # Se houver elementos restantes, adiciona-os à última sublista
    if len(numeros) % num_partes != 0:
        sublistas[-1].extend(numeros[num_partes * tamanho_parte:])

    # Usa um Pool de processos para calcular a soma de cada sublista em paralelo
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Mapear a função soma_parcial para cada sublista
        resultados = list(executor.map(soma_parcial, sublistas))

    # Calcula a soma total somando os resultados parciais
    soma_total = sum(resultados)

    print(f"A soma total é: {soma_total}")
