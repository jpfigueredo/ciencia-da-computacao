import socket
import ssl
from ssl import SSLSocket

original_send = SSLSocket.send
original_recv = SSLSocket.recv

def send_com_log(self, data, *args, **kwargs):
    print(f"Interceptado (envio): {data}")
    return original_send(self, data, *args, **kwargs)

def recv_com_log(self, *args, **kwargs):
    data = original_recv(self, *args, **kwargs)
    print(f"Interceptado (recebido): {data}")
    return data

SSLSocket.send = send_com_log
SSLSocket.recv = recv_com_log

def cliente_tls_com_logging():
    HOST = 'myserver'
    PORT = 12346

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            ssock.connect((HOST, PORT))
            print("Cliente conectado ao servidor TLS.")

            mensagem = b"Mensagem segura com logging de pacotes"
            ssock.send(mensagem)
            
            resposta = ssock.recv(1024)
            print("Resposta do servidor:", resposta.decode())

if __name__ == "__main__":
    cliente_tls_com_logging()







