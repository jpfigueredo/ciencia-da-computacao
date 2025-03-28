import socket
import ssl

HOST = 'myserver'
PORT = 12346

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.connect((HOST, PORT))
        print("Cliente: conexão estabelecida")

        mensagem = "Olá, servidor TLS!"
        ssock.send(mensagem.encode())
        print(f"Cliente: enviado: {mensagem}")

        resposta = ssock.recv(1024)
        print(f"Cliente: recebido: {resposta.decode()}")
