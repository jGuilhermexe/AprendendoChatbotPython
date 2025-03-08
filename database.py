from pymongo import MongoClient

def conectar_bd():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ChatbotTelegram"]
    return db

def salvar_mensagem(usuario_id, nome, mensagem):
    db = conectar_bd()
    colecao = db["mensagens"] 
    

    documento = {
        "usuario_id": usuario_id,
        "nome": nome,
        "mensagem": mensagem
    }
    
    colecao.insert_one(documento)