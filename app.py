from flask import Flask, jsonify, render_template
from database import conectar_bd

app = Flask(__name__)

@app.route("/historico", methods=["GET"])
def historico():
    conexao = conectar_bd()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT usuario_id, nome, mensagem, data FROM mensagens ORDER BY data DESC")
    mensagens = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(mensagens)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
