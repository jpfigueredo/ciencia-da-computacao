import ipaddress

def verificar_ip_em_prefixo(ip, prefixo):
    try:
        ip_obj = ipaddress.ip_address(ip)
        prefixo_obj = ipaddress.ip_network(prefixo, strict=False)
        return ip_obj in prefixo_obj
    except ValueError:
        return False

# Exemplo de uso
ip = "192.168.1.5"
prefixo = "192.168.1.0/24"
if verificar_ip_em_prefixo(ip, prefixo):
    print(f"O IP {ip} está dentro do prefixo {prefixo}.")
else:
    print(f"O IP {ip} NÃO está dentro do prefixo {prefixo}.")
