from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL')

@app.route('/')
def index():
    return "Backend Flask rodando com sucesso!"

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    # lógica simples de adivinhação (exemplo)
    number = int(data.get("number"))
    if number == 42:
        return jsonify(result="correct"), 200
    return jsonify(result="try again"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)