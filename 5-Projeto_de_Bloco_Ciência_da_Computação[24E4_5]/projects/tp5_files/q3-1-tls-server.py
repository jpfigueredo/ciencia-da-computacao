import socket
import ssl

HOST = '0.0.0.0'
PORT = 12345

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    print("Servidor aguardando conexões...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f"Conexão estabelecida com {addr}")

        data = conn.recv(1024)
        print(f"Recebido: {data.decode()}")

        conn.send(data)
        conn.close()
