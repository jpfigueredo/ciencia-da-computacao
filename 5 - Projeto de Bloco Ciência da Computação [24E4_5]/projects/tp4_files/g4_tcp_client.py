import socket

def cliente_tcp(host='127.0.0.1', porta=5000):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, porta))
            resposta = s.recv(1024).decode()
            print("Resposta do servidor:", resposta)
    except ConnectionRefusedError:
        print("Erro: Servidor não encontrado. Verifique se o servidor está em execução.")

if __name__ == "__main__":
    cliente_tcp()
