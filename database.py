from pymongo import MongoClient

def conectar_bd():
    client = MongoClient("mongodb://localhost:27017/")  # Conecta ao servidor MongoDB
    db = client["ChatbotTelegram"]  # Seleciona o banco de dados (será criado se não existir)
    return db

def salvar_mensagem(usuario_id, nome, mensagem):
    db = conectar_bd()
    colecao = db["mensagens"]  # Seleciona a coleção
    
    # Cria um documento
    documento = {
        "usuario_id": usuario_id,
        "nome": nome,
        "mensagem": mensagem
    }
    
    colecao.insert_one(documento)