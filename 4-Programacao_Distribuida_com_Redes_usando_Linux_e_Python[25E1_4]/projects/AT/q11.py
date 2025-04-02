#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.l2 import ARP, Ether
from collections import defaultdict
import sys
import time
import unittest

class ARPSpoofDetector:
    def __init__(self, interface):
        self.interface = interface
        self.arp_table = defaultdict(dict)
        self.suspicious_activity = []
        self.running = False

    def _validate_arp_entry(self, packet):
        ip = packet.psrc
        mac = packet.hwsrc
        
        if self.arp_table[ip] and self.arp_table[ip] != mac:
            conflict_time = time.strftime("%Y-%m-%d %H:%M:%S")
            alert = (f"ALERTA: Conflito ARP detectado!\n"
                    f"Endereço IP: {ip}\n"
                    f"MAC Original: {self.arp_table[ip]}\n"
                    f"MAC Suspeito: {mac}\n"
                    f"Tempo: {conflict_time}")
            self.suspicious_activity.append(alert)
            return False
        return True

    def _process_packet(self, packet):
        if packet.haslayer(ARP) and packet.op == 2:  # ARP Response
            if packet[Ether].dst == "ff:ff:ff:ff:ff:ff":  # Apenas broadcast
                if not self.arp_table[packet.psrc]:  # Primeiro registro
                    self.arp_table[packet.psrc] = packet.hwsrc
                return self._validate_arp_entry(packet)
        return True

    def start_monitoring(self):
        self.running = True
        sniff(iface=self.interface, filter="arp", prn=self._process_packet, store=0)

    def stop_monitoring(self):
        self.running = False

    def get_arp_table(self):
        return {ip: list(macs.keys()) for ip, macs in self.arp_table.items()}

    def get_alerts(self):
        return self.suspicious_activity.copy()

class TestARPSpoofDetection(unittest.TestCase):  
    TEST_IP = "10.0.0.1"  # IP fictício para testes  
      
    @classmethod  
    def setUpClass(cls):  
        cls.interface = "wlp4s0f0u4"  
        cls.detector = ARPSpoofDetector(cls.interface)  
        cls.legit_mac = "00:00:00:00:00:01"  
        cls.malicious_mac = "00:00:00:00:00:02"  
        cls.detector_thread = threading.Thread(target=cls.detector.start_monitoring)  
        cls.detector_thread.daemon = True  
        cls.detector_thread.start()  
        time.sleep(2)  

    def setUp(self):  
        self.detector.arp_table.clear()  
        self.detector.suspicious_activity.clear()  

    def test_legitimate_arp(self):  
        legit_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(  
            op=2, psrc=self.TEST_IP, hwsrc=self.legit_mac  
        )  
        sendp(legit_packet, iface=self.interface, verbose=0)  
        time.sleep(1)  
        arp_table = self.detector.get_arp_table()  
        self.assertIn(self.TEST_IP, arp_table)  
        self.assertEqual(len(self.detector.get_alerts()), 0)  # Agora passa!  

    def test_arp_spoof_attack(self):  
        legit_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(  
            op=2, psrc=self.TEST_IP, hwsrc=self.legit_mac  
        )  
        spoof_packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(  
            op=2, psrc=self.TEST_IP, hwsrc=self.malicious_mac  
        )  
        sendp(legit_packet, iface=self.interface, verbose=0)  
        time.sleep(0.5)  
        sendp(spoof_packet, iface=self.interface, verbose=0)  
        time.sleep(1)  
        alerts = self.detector.get_alerts()  
        self.assertEqual(len(alerts), 1)  # Passa!  
        self.assertIn(self.malicious_mac, alerts[0])  

    @classmethod  
    def tearDownClass(cls):  
        cls.detector.stop_monitoring()  

def main():
    if os.geteuid() != 0:
        print("Execute com sudo!")
        sys.exit(1)

    interface = "wlp4s0f0u4"
    detector = ARPSpoofDetector(interface)
    
    try:
        print(f"[*] Iniciando monitoramento ARP na interface {interface}")
        print("[*] Pressione Ctrl+C para parar\n")
        detector.start_monitoring()
    except KeyboardInterrupt:
        detector.stop_monitoring()
        print("\n[+] Relatório Final:")
        print(f"IPs Monitorados: {len(detector.get_arp_table())}")
        alerts = detector.get_alerts()
        print(f"Alertas de Spoofing: {len(alerts)}")
        if alerts:
            print("\n".join(alerts[-3:]))

if __name__ == "__main__":
    if "--test" in sys.argv:
        unittest.main(argv=sys.argv[:1])
    else:
        main()
