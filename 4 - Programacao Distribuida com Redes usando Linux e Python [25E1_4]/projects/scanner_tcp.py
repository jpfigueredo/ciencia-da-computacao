import socket
import threading
import time
from queue import Queue
import argparse

parser = argparse.ArgumentParser(description='Port Scanner TCP')
parser.add_argument('target', help='Endereço IP ou hostname do alvo')
parser.add_argument('-p', '--ports', type=int, nargs=2, metavar=('START', 'END'), 
                    default=[1, 1024], help='Intervalo de portas (padrão: 1-1024)')
parser.add_argument('-t', '--threads', type=int, default=100, 
                    help='Número de threads (padrão: 100)')
parser.add_argument('-T', '--timeout', type=float, default=1.5, 
                    help='Timeout da conexão em segundos (padrão: 1.5)')
args = parser.parse_args()

target = args.target
start_port, end_port = args.ports
threads = args.threads
timeout = args.timeout
queue = Queue()
open_ports = []

def resolve_target():
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print("Erro: Hostname não resolvido.")
        exit(1)

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"Porta {port}: ABERTA")
    except (socket.timeout, ConnectionRefusedError):
        pass
    except Exception as e:
        print(f"Erro na porta {port}: {str(e)}")

def worker():
    while True:
        port = queue.get()
        scan_port(port)
        queue.task_done()

def main():
    global target_ip
    target_ip = resolve_target()
    print(f"\n[*] Escaneando {target} ({target_ip}) (portas {start_port}-{end_port})...\n")
    
    start_time = time.time()
    
    for _ in range(threads):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
    
    for port in range(start_port, end_port + 1):
        queue.put(port)
    
    queue.join()
    
    print(f"\n[*] Escaneamento concluído em {time.time() - start_time:.2f} segundos.")
    print(f"[*] Portas abertas: {sorted(open_ports)}")

if __name__ == "__main__":
    main()
