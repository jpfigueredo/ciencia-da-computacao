import time

# Lista de prefixos para busca linear
prefixos = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"] * 1000

def busca_linear(ip):
    for prefixo in prefixos:
        if verificar_ip_em_prefixo(ip, prefixo):
            return prefixo
    return None

# Medindo o tempo de execução da busca linear
inicio = time.time()
ip = "192.168.1.55"
prefixo = busca_linear(ip)
fim = time.time()
print(f"Busca linear levou {fim - inicio:.6f} segundos.")

# Medindo o tempo de execução da busca utilizando Trie
trie = Trie()
for prefixo in prefixos:
    trie.inserir(prefixo)

inicio = time.time()
prefixo = trie.buscar(ip)
fim = time.time()
print(f"Busca utilizando Trie levou {fim - inicio:.6f} segundos.")
