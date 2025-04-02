import socket

def servidor_udp(host='0.0.0.0', porta=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, porta))
        print(f"Servidor UDP ouvindo em {host}:{porta}...")
        while True:
            dados, endereco = s.recvfrom(1024)
            print(f"Recebido de {endereco}: {dados.decode()}")
            s.sendto(b"ack\n", endereco)

if __name__ == "__main__":
    servidor_udp()
