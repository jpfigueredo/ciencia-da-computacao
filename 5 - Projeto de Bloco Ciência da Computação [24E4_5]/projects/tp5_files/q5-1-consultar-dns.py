import dns.resolver

def consultar_dns(dominio):
    try:
        print("Registros A:")
        registros_a = dns.resolver.resolve(dominio, 'A')
        for registro in registros_a:
            print(f"\t{registro.address}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("\tNenhum registro A encontrado.")

    try:
        print("\nRegistros MX:")
        registros_mx = dns.resolver.resolve(dominio, 'MX')
        for registro in registros_mx:
            print(f"\t{registro.preference} {registro.exchange}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("\tNenhum registro MX encontrado.")

    try:
        print("\nRegistros NS:")
        registros_ns = dns.resolver.resolve(dominio, 'NS')
        for registro in registros_ns:
            print(f"\t{registro.target}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("\tNenhum registro NS encontrado.")

if __name__ == "__main__":
    dominio = input("Digite o domínio (ex: example.com): ").strip()
    consultar_dns(dominio)
