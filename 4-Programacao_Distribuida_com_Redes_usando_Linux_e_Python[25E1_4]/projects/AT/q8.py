#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.sendrecv import send, sniff, sr1
from scapy.packet import Raw
import time

def capturar_pacotes(interface, tempo=10):
    print(f"Capturando pacotes na interface {interface} por {tempo} segundos...")
    pacotes = sniff(iface=interface, timeout=tempo)
    print(f"Captura concluída. {len(pacotes)} pacotes capturados.")
    return pacotes

def analisar_pacote(pacote):
    print("\n[+] Análise do pacote:")
    
    if Ether in pacote:
        print(f"MAC Origem: {pacote[Ether].src} -> MAC Destino: {pacote[Ether].dst}")
    
    if IP in pacote:
        print(f"IP Origem: {pacote[IP].src}:{pacote[IP].sport}")
        print(f"IP Destino: {pacote[IP].dst}:{pacote[IP].dport}")
        print(f"Protocolo: {pacote[IP].proto}")
        print(f"TTL: {pacote[IP].ttl}")
    
    if TCP in pacote:
        print("Camada TCP:")
        print(f"Flags: {pacote[TCP].flags}")
        print(f"Sequência: {pacote[TCP].seq}")
    
    if Raw in pacote:
        print(f"Payload ({len(pacote[Raw])} bytes): {pacote[Raw].load[:50]}...")

def modificar_e_injetar(pacote, interface):
    try:
        novo_pacote = pacote.copy()
        
        novo_pacote[Ether].src, novo_pacote[Ether].dst = novo_pacote[Ether].dst, novo_pacote[Ether].src
        
        if IP in novo_pacote:
            novo_pacote[IP].src, novo_pacote[IP].dst = novo_pacote[IP].dst, novo_pacote[IP].src
            novo_pacote[IP].ttl = 128
            
            if TCP in novo_pacote:
                novo_pacote[TCP].sport = 8080  # Nova porta
            elif UDP in novo_pacote:
                novo_pacote[UDP].sport = 8080
        
        print("\n[!] Pacote modificado:")
        novo_pacote.show()
        
        sendp(novo_pacote, iface=interface, verbose=False)
        print("\n[+] Pacote modificado injetado com sucesso!")
    
    except Exception as e:
        print(f"Erro na modificação: {e}")

def injetar_ping_falso(interface, destino):
    pacote = Ether()/IP(dst=destino)/ICMP(type=8)/Raw(load="Mensagem Falsa!")
    sendp(pacote, iface=interface, verbose=False)
    print(f"\n[+] Pacote ICMP falso enviado para {destino}")

def testar_captura(interface):
    print("\n=== Teste de Captura ===")
    pacotes = capturar_pacotes(interface, 5)
    if len(pacotes) > 0:
        analisar_pacote(pacotes[0])
        return True
    return False

def testar_injecao(interface):
    """Teste de injeção de pacotes"""
    print("\n=== Teste de Injeção ===")
    destino = "8.8.8.8"
    injetar_ping_falso(interface, destino)
    return True

def main():
    interface = "enp6s0"  # Altere para sua interface de rede
    
    while True:
        print("\n=== Menu Scapy ===")
        print("1. Capturar e analisar pacotes")
        print("2. Modificar e injetar pacote")
        print("3. Executar testes completos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            pacotes = capturar_pacotes(interface)
            if pacotes:
                analisar_pacote(pacotes[0])
        
        elif opcao == "2":
            pacotes = capturar_pacotes(interface, 5)
            if pacotes:
                modificar_e_injetar(pacotes[0], interface)
        
        elif opcao == "3":
            if testar_captura(interface) and testar_injecao(interface):
                print("\n[✓] Todos os testes foram bem-sucedidos!")
        
        elif opcao == "4":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()