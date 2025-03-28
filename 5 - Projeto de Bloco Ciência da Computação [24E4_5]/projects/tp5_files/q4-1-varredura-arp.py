from scapy.all import ARP, Ether, srp

def varredura_arp(rede):
    pacote_arp = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rede)
    resposta, _ = srp(pacote_arp, timeout=3, verbose=0)
    print("Hosts ativos na rede:")
    for pacote in resposta:
        print(f"IP: {pacote[1].psrc} \t MAC: {pacote[1].hwsrc}")

if __name__ == "__main__":
    varredura_arp("192.168.1.0/24")
