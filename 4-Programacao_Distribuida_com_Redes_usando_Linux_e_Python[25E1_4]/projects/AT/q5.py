import socket  

def servidor_tcp(host='127.0.0.1', porta=8000):  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
        s.bind((host, porta))  
        s.listen()  
        print(f"Servidor ouvindo em {host}:{porta}...")  
        while True:  
            conn, addr = s.accept()  
            with conn:  
                print(f"Conexão estabelecida com {addr}")  
                dados = conn.recv(1024).decode()  
                print(f"Requisição recebida:\n{dados}")  
                caminho = dados.split()[1]  
                if caminho == '/':  
                    resposta = (  
                        "HTTP/1.1 200 OK\n"  
                        "Content-Type: text/html\n\n"  
                        "<html><body><h1>Servidor Funcionando!</h1></body></html>"  
                    )  
                else:  
                    resposta = (  
                        "HTTP/1.1 404 Not Found\n"  
                        "Content-Type: text/html\n\n"  
                        "<html><body><h1>Erro 404: Página não encontrada</h1></body></html>"  
                    )  
                conn.sendall(resposta.encode())  

if __name__ == "__main__":  
    servidor_tcp()