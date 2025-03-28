from scapy.all import sniff, ARP
from collections import defaultdict
import time
import netifaces
import ipaddress
import signal
import sys

INTERFACE = "wlp4s0f0u1"
SUBREDE = None

ip_mac_mappings = defaultdict(lambda: {"mac": None, "timestamp": None})

def configurar_subrede():
    global SUBREDE
    try:
        addrs = netifaces.ifaddresses(INTERFACE)
        ip_info = addrs[netifaces.AF_INET][0]
        ip = ip_info['addr']
        netmask = ip_info['netmask']
        SUBREDE = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
        print(f"[*] Monitorando subrede: {SUBREDE}")
    except Exception as e:
        print(f"[ERRO] Falha ao detectar subrede: {e}")
        sys.exit(1)

def process_packet(packet):
    if packet.haslayer(ARP):
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ipaddress.IPv4Address(ip) not in SUBREDE:
            return

        if ip_mac_mappings[ip]["mac"] is not None:
            mac_anterior = ip_mac_mappings[ip]["mac"]
            if mac_anterior != mac:
                print(f"\n[!] ALERTA: Possível ARP Spoofing detectado!")
                print(f"    IP: {ip}")
                print(f"    MAC anterior: {mac_anterior}")
                print(f"    MAC atual: {mac}")
                print(f"    Interface: {INTERFACE}\n")

        ip_mac_mappings[ip]["mac"] = mac
        ip_mac_mappings[ip]["timestamp"] = time.time()

def shutdown(sig, frame):
    print("\n[*] Encerrando monitoramento...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    configurar_subrede()
    print(f"[*] Iniciando monitoramento ARP em {INTERFACE} (Ctrl+C para parar)")
    sniff(filter="arp", prn=process_packet, store=0, iface=INTERFACE)