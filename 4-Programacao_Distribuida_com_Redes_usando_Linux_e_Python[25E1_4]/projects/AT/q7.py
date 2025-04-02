import pcapy
import sys
import time

def listar_interfaces():
    dispositivos = pcapy.findalldevs()
    if not dispositivos:
        print("Nenhuma interface de rede encontrada.")
        sys.exit(1)
    print("Dispositivos disponíveis:", dispositivos)
    return dispositivos

def capturar_pacote(interface):
    cap = pcapy.open_live(interface, 65536, True, 100)
    print(f"\nCapturando pacotes na interface {interface} (pressione Ctrl+C para parar)...")
    try:
        (cabecalho, pacote) = cap.next()
        if pacote:
            print("Pacote capturado (em hexadecimal):")
            print(pacote.hex())
        else:
            print("Nenhum pacote capturado.")
    except KeyboardInterrupt:
        print("\nInterrupção manual da captura.")

def injetar_pacote(interface, pacote_data):
    cap = pcapy.open_live(interface, 65536, True, 100)
    try:
        cap.sendpacket(pacote_data)
        print("Pacote injetado com sucesso!")
    except Exception as e:
        print("Erro ao injetar pacote:", e)

def criar_ethernet_frame():
    dst_mac = b'\xff\xff\xff\xff\xff\xff'       # Broadcast
    src_mac = b'\x00\x0a\x95\x9d\x68\x16'       # Exemplo de MAC
    eth_type = b'\x08\x00'                      # EtherType para IPv4
    payload = b'Hello, this is a test packet from pcapy-ng'
    frame = dst_mac + src_mac + eth_type + payload
    return frame

if __name__ == "__main__":
    dispositivos = listar_interfaces()
    interface = dispositivos[0]
    print("Utilizando a interface:", interface)

    pacote = criar_ethernet_frame()
    print("\nInjetando pacote na interface...")
    injetar_pacote(interface, pacote)
    
    time.sleep(2)
    
    capturar_pacote(interface)
