import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jean2706!", 
        database="bot_naps"
    )

def salvar_mensagem(usuario_id, nome, mensagem):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO mensagens (usuario_id, nome, mensagem) VALUES (%s, %s, %s)", 
                   (usuario_id, nome, mensagem))
    conexao.commit()
    cursor.close()
    conexao.close()
