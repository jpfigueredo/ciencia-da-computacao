import nmap

def scan_sincrono(target, ports):
    print(f"\nScan síncrono iniciado em {target} (portas: {ports})")
    nm = nmap.PortScanner()
    nm.scan(hosts=target, ports=ports)

    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"Status: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocolo: {proto}")
            portas_abertas = nm[host][proto].keys()
            for porta in sorted(portas_abertas):
                estado = nm[host][proto][porta]['state']
                print(f"Porta {porta}: {estado}")

def scan_assincrono(target, ports):
    print(f"\nScan assíncrono iniciado em {target} (portas: {ports})")
    nm = nmap.PortScannerAsync()

    def callback_result(host, result):
        print(f"\nCallback: Resultados recebidos para {host}")

        if host in result['scan']:
            host_info = result['scan'][host]
            hostname = host_info['hostnames'][0]['name']
            print(f"\nHost: {host} ({hostname})")
            print(f"Status: {host_info['status']['state']}")

            if 'tcp' in host_info:
                print("\nProtocolo: tcp")
                for porta, info in sorted(host_info['tcp'].items()):
                    print(f"Porta {porta}: {info['state']}")

    nm.scan(hosts=target, ports=ports, callback=callback_result)

    while nm.still_scanning():
        print("Aguardando término do scan...")
        nm.wait(5)

if __name__ == "__main__":
    print("\nTeste Síncrono")
    scan_sincrono('scanme.nmap.org', '20-80')

    print("\nTeste Assíncrono")
    scan_assincrono('scanme.nmap.org', '20-80')