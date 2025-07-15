from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id":1, "nome":"Maria"},
    {"id":2, "nome":"Bruno"}
]

@app.route('/')
def home():
    return "Bem-vindo à API"

@app.route('/usuarios',methods=['GET'])
def listar_usarios():
    return jsonify(usuarios)

@app.route('/registrar',methods=['POST'])
def adicionar_usuario():
    novo = request.get_json()
    usuarios.append(novo)
    return jsonify(novo),201

if __name__ == '__main__':
    app.run(debug=True)

#Test api
#bash:
#curl -X POST http://127.0.0.1:5000/registrar -H "Content-Type: application/json" -d '{"id": 3, "nome": "Romulo"}'