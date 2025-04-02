import socket

def cliente_udp(host='127.0.0.1', porta=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"teste", (host, porta))
        resposta, _ = s.recvfrom(1024)
        print("Resposta:", resposta.decode())

if __name__ == "__main__":
    cliente_udp()
