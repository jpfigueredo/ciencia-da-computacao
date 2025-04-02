#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from collections import defaultdict
import time
import signal
import sys

class TransferDetector:
    def __init__(self, interface, threshold=100, timeout=60):
        self.interface = interface
        self.threshold = threshold
        self.timeout = timeout
        self.connections = defaultdict(lambda: {'packets': 0, 'bytes': 0, 'start_time': time.time()})
        self.running = True

    def detect_transfer(self, pkt):
        try:
            if IP in pkt:
                src = pkt[IP].src
                dst = pkt[IP].dst
                proto = pkt[IP].proto
                
                key = (src, dst, proto)
                
                self.connections[key]['packets'] += 1
                self.connections[key]['bytes'] += len(pkt)
                
                if self.connections[key]['packets'] >= self.threshold:
                    self.alert_transfer(key)
                    del self.connections[key]

                self.cleanup_connections()

        except Exception as e:
            print(f"Erro na análise: {e}")

    def alert_transfer(self, key):
        src, dst, proto = key
        stats = self.connections[key]
        duration = time.time() - stats['start_time']
        
        print(f"\n[!] TRANSFERÊNCIA DETECTADA [!]")
        print(f"Origem: {src} -> Destino: {dst}")
        print(f"Protocolo: {self.get_proto_name(proto)}")
        print(f"Pacotes: {stats['packets']} | Bytes: {stats['bytes']}")
        print(f"Duração: {duration:.2f} segundos")
        print("-" * 50)
        
        # Registrar em log
        with open("transfer_log.txt", "a") as f:
            f.write(f"{time.ctime()} - Transferência detectada: {src} -> {dst} | "
                    f"Proto: {self.get_proto_name(proto)} | "
                    f"Packets: {stats['packets']} | Bytes: {stats['bytes']}\n")

    def get_proto_name(self, proto):
        return {
            6: "TCP",
            17: "UDP",
            1: "ICMP"
        }.get(proto, "Desconhecido")

    def cleanup_connections(self):
        now = time.time()
        to_delete = [k for k, v in self.connections.items() 
                    if (now - v['start_time']) > self.timeout]
        for k in to_delete:
            del self.connections[k]

    def start(self):
        print(f"Iniciando monitoramento na interface {self.interface}...")
        print(f"Limiar: {self.threshold} pacotes | Janela temporal: {self.timeout}s")
        sniff(iface=self.interface, prn=self.detect_transfer, store=0)

    def signal_handler(self, sig, frame):
        print("\nEncerrando monitoramento...")
        self.running = False
        sys.exit(0)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Detector de transferências de rede")
    parser.add_argument("-i", "--interface", required=True, help="Interface de rede")
    parser.add_argument("-t", "--threshold", type=int, default=100, 
                       help="Limiar de pacotes para detecção")
    parser.add_argument("-w", "--window", type=int, default=60, 
                       help="Janela temporal em segundos")
    
    args = parser.parse_args()
    
    detector = TransferDetector(
        interface=args.interface,
        threshold=args.threshold,
        timeout=args.window
    )
    
    signal.signal(signal.SIGINT, detector.signal_handler)
    detector.start()