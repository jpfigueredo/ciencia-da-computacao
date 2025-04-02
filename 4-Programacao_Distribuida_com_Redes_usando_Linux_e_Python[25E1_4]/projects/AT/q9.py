#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
import sys
import time

def verifica_host(ip):
    pacote = IP(dst=ip)/ICMP()
    resposta = sr1(pacote, timeout=2, verbose=0)
    return resposta is not None

def scan_porta_tcp_syn(ip, porta, timeout=1):
    pacote = IP(dst=ip)/TCP(dport=porta, flags="S")
    resposta = sr1(pacote, timeout=timeout, verbose=0)
    
    if resposta is None:
        return "filtered"
    elif resposta.haslayer(TCP):
        if resposta[TCP].flags == 0x12:
            send(IP(dst=ip)/TCP(dport=porta, flags="R"), verbose=0) 
            return "open"
        elif resposta[TCP].flags == 0x14:
            return "closed"
    return "filtered"

def scan_porta_udp(ip, porta, timeout=2):
    pacote = IP(dst=ip)/UDP(dport=porta)/Raw(load="teste")
    resposta = sr1(pacote, timeout=timeout, verbose=0)
    
    if resposta is None:
        return "open|filtered"
    elif resposta.haslayer(ICMP):
        if resposta[ICMP].type == 3 and resposta[ICMP].code in [1, 2, 9, 10, 13]:
            return "closed"
    return "open|filtered"

def scan_intervalo_portas(ip, tecnica, portas, timeout=1):
    resultados = {}
    print(f"\n[*] Iniciando escaneamento {tecnica} em {ip}...")
    
    for porta in portas:
        if tecnica == "tcp":
            status = scan_porta_tcp_syn(ip, porta, timeout)
        elif tecnica == "udp":
            status = scan_porta_udp(ip, porta, timeout)
        
        resultados[porta] = status
        print(f"Porta {porta}: {status}")
        time.sleep(0.1)
    
    return resultados

def exemplo_uso():
    # Teste básico
    alvo = "127.0.0.1"  # Substitua por IP válido
    portas = range(80, 85)  # Portas 80-84
    
    if not verifica_host(alvo):
        print(f"Host {alvo} inacessível!")
        return
    
    print(f"\n=== Teste TCP SYN Scan ===")
    resultados_tcp = scan_intervalo_portas(alvo, "tcp", portas)
    
    print(f"\n=== Teste UDP Scan ===")
    resultados_udp = scan_intervalo_portas(alvo, "udp", [53, 123, 161])
    
    print("\nResumo TCP:")
    for porta, status in resultados_tcp.items():
        print(f"Porta {porta}/TCP: {status}")
    
    print("\nResumo UDP:")
    for porta, status in resultados_udp.items():
        print(f"Porta {porta}/UDP: {status}")

if __name__ == "__main__":
    # Execução via linha de comando
    if len(sys.argv) != 4:
        print(f"Uso: {sys.argv[0]} <IP> <tcp|udp> <porta-range>")
        print("Exemplo: sudo python3 scanner.py 192.168.1.1 tcp 80-100")
        sys.exit(1)
    
    ip = sys.argv[1]
    tecnica = sys.argv[2].lower()
    faixa = sys.argv[3]
    
    # Parse da faixa de portas
    if '-' in faixa:
        inicio, fim = map(int, faixa.split('-'))
        portas = range(inicio, fim+1)
    else:
        portas = [int(faixa)]
    
    if not verifica_host(ip):
        print(f"Host {ip} não responde a ping!")
        sys.exit(2)
    
    resultados = scan_intervalo_portas(ip, tecnica, portas)
    
    print("\n[+] Resultado final:")
    for porta, status in resultados.items():
        print(f"Porta {porta}: {status}")