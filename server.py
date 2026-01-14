from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "Servidor online! 🚀"})

@app.route('/status')
def status():
    return jsonify({"status": "ativo", "plataforma": "gratuita"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
