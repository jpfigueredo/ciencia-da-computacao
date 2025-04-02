# Client TCP
import socket

HOST = '127.0.0.1'
PORT = 5000 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    mensagem = 'Olá, servidor!'
    s.sendall(mensagem.encode())
    data = s.recv(1024)

print(f"Mensagem recebida do servidor: {data.decode()}")