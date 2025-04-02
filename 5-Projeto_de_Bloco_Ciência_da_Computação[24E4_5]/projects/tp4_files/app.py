from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    dados = request.get_data().decode()
    return f"Dados recebidos: {dados}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)