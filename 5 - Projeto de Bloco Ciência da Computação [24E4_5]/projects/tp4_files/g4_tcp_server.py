import socket

def servidor_tcp(host='127.0.0.1', porta=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, porta))
        s.listen()
        print(f"Servidor TCP ouvindo em {host}:{porta}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Conexão estabelecida com {addr}")
            conn.sendall(b"Bem-vindo ao servidor TCP!\n")


if __name__ == "__main__":
    servidor_tcp()
