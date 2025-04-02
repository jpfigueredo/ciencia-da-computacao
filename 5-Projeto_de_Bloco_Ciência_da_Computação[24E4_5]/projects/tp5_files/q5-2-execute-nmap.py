import subprocess
import sys

def executar_nmap(host):
    try:
        comando = ["nmap", "-sV", "-Pn", host]
        resultado = subprocess.run(
            comando, 
            capture_output=True, 
            text=True, 
            check=True
        )
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar Nmap: {e.stderr}")
    except FileNotFoundError:
        print("Nmap não está instalado. Instale com: sudo apt install nmap")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nmap_scan.py <host>")
        sys.exit(1)
    
    host = sys.argv[1]
    executar_nmap(host)
