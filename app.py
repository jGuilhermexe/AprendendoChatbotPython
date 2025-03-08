from flask import Flask, render_template
from pymongo import MongoClient
import telebot
import threading
import time

app = Flask(__name__)


CHAVE_API = "7710595076:AAFG6mQk6dRU5N-PVN5HIBSdDaM4imgwnes"
bot = telebot.TeleBot(CHAVE_API)


usuarios_desabafo = {}


def conectar_bd():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ChatbotTelegram"]
    return db


@app.route('/')
def index():
    db = conectar_bd()
    colecao = db["mensagens"]
    mensagens = list(colecao.find({}, {"_id": 0})) 
    return render_template('index.html', mensagens=mensagens)


@bot.message_handler(commands=["PrincipaisLinks"])
def PrincipaisLinks(mensagem):
    texto = """
    Conheça os principais links da universidade, onde você pode ter acesso a informações de extrema importância! 😁
    💠 Site da Unidade Acadêmica de Belo Jardim - uabj.ufrpe.br
    💠 Site da Universidade Federal Rural de Pernambuco - ufrpe.br
    
    O Menu do Estudante trás MUITAS INFORMAÇÕES que podem ser utéis para sanar diversas dúvidas.
    Inclusive, dúvidas com relações a bolsas, auxílios e valores, podem ser encontrados por lá.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Bolsas"])
def PEnoCampus(mensagem):
    texto = """
    A UABJ conta com diversos tipos de auxílios sendo eles:
    ⚜️ Programa de Apoio ao Discente (PAI)
    ⚜️ Programa de Promoção ao Esporte (PPE)
    ⚜️ Programa de Apoio a Gestante (PAG)
    ⚜️ Programa de Bolsa Permanência (PBP)
    ⚜️ Auxílio Moradia
    ⚜️ Auxílio Higiene Menstrual
    ⚜️ Auxílio de Atenção à Saúde
    
    -------------------------------------
     ⁉️ DÚVIDAS FREQUENTES ⁉️ :

    📌 É possivel acumular as bolsas da Assistência Estudantil? 
    Não, a única bolsa acumulável é a do Programa de Apoio a Gestante (PAG). Porém, só se a dicente já for bolsista e se tornar mãe durante a graduação, ela terá direito apenas a 50% do "Auxílio Creche" (PAG)
    
    📌 É possível acumular o PE no Campus com as bolsas do Auxílio Estudantil?
    Sim, é possível acumular PE no Campus com as bolsas do Auxílio Estudantil.
    
    📌 Quais os valores das Bolsas/Auxílios?
    Todos os valores e condições estão disponíveis no site da universidade (uabj.ufrpe.br). Acesse o site, role até a área "Estudante" e clique em "Assistência Estudantil na UABJ".
    
    📌 Como faço pra ver os editais de lançamentos de Bolsas e Auxílios?
    Tanto o site da UFRPE, quanto da UABJ lançam os editais, mas recomendamos sempre estar de olho no site da UFRPE (ufrpe.br)
    Acesse o site > Procure o tópico Institucional > Clique em Pró-Reitorias > Clique em Pró-Reitoria de Gestão Estudantil e Inclusão - PROGESTI 
    Assim, você consegue ver pelo banner e a área de notícias todos os editais e lançamentos.

    📌 Qual a documentação necessária para solicitar um auxílio/bolsa?
    Existe um guia para auxíliar nas inscrições das bolsas, ele é bem flexível e quase todas as inscrições podem ser feitas a partir dele:
    Acesse o link do PDF a seguir: (https://www.progesti.ufrpe.br/sites/www.progesti.ufrpe.br/files/Guia%20da%20Assistência%20Estudantil.pdf)
    Nesse PDF contem todas as instruções necessárias para a documentação e solicitação das bolsas da universidade.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["DuvidasGerais"])
def DuvidasGerais(mensagem):
    texto = """
📌 A universidade possui Residência Estudantil?
    Não. Nossa universidade não possui residência estudantil. A UABJ é uma universidade nova, e o Campus ainda segue em processo de construção, porém, nós possuímos auxílio moradia
    justamente para suprir essa falta.

📌 A universidade possui Restaurante Universitário (RU)?
    Não. A UABJ é uma universidade nova, e tanto o RU quanto o Campus ainda segue em processo de construção.

📌 Onde as aulas ocorrem?
    As nossas aulas ocorrem na Unidade Provisória UABJ onde se encontram os laboratórios do curso, biblioteca, escolaridade e o NAPS, e na AEB (Autarquia Educacional de Belo Jardim)
    Aconselhamos que você entre em contato com a escolaridade para informações maiores com relação ao curso, aulas e transporte.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Certo, você necessita de ajuda no quesito "Bolsas e Auxílios"
Selecione um tópico que seja de seu interesse (Clique no item):
    /PrincipaisLinks
    /Bolsas
    /DuvidasGerais
Responder qualquer outra coisa não irá funcionar, por favor, clique em uma das opções:
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    💛 O NAPS (Núcleo de Apoio Psicopedagógico e Social) é o setor presente em nossa universidade que tem como objetivo oferecer suporte aos estudantes em diversas áreas,
    visando promover o bem-estar e o sucesso acadêmico. O NAPS oferece serviços de apoio social, psicológico, inclusão e acessibilidade e orientação profissional.
    -------------------------------------

     ⁉️ DÚVIDAS FREQUENTES ⁉️ :

    📌 Onde se localiza o NAPS da UABJ?
    O NAPS está localizado no prédio provisório da UABJ. Aqui você encontra profissionais bem preparados pra te auxiliar no que for necessário, como psicólogo, assistente social, enfermeiras e outros profissionais a sua disposição! 😁

    📌 Como faço o agendamento com o psicólogo?
    O atual agendamento está sendo feito diretamente com o psicólogo, a partir do seu número de telefone, ou enviando um e-mail. Telefone: (82) 9 9939-5512 . E-mail: psicologiauabj@ufrpe.br . Nossa plataforma de agendamento online segue em desenvolvimento.
    """ 
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    usuarios_desabafo[mensagem.chat.id] = True  
    bot.send_message(mensagem.chat.id, "Sinta-se à vontade para desabafar. Estou aqui para ouvir. ❤️\n\nDigite sua mensagem:")

@bot.message_handler(func=lambda mensagem: mensagem.chat.id in usuarios_desabafo)
def desabafo(mensagem):
    db = conectar_bd()
    colecao = db["mensagens"]
    colecao.insert_one({
        "usuario_id": mensagem.chat.id,
        "nome": mensagem.from_user.first_name,
        "mensagem": mensagem.text
    })
    bot.send_message(mensagem.chat.id, "Nós recebemos a sua mensagem. Se você precisar de um suporte maior, entre em contato com nosso psicólogo do NAPS, ou acesse nossa plataforma do ATENDINAPS - UABJ. 💙")
    
    del usuarios_desabafo[mensagem.chat.id]

    responder(mensagem)

def verificar(mensagem):
    return mensagem.chat.id not in usuarios_desabafo

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Seja bem-vindo ao Bot AtendiNAPS - UABJ!
Selecione um tópico que seja de seu interesse (Clique no item):
    /opcao1 Dúvidas relacionadas a Bolsas/Auxílios e Dúvidas Gerais
    /opcao2 Dúvidas relacionadas ao NAPS
    /opcao3 Gostaria de Desabafar
Responder qualquer outra coisa não irá funcionar, por favor, clique em uma das opções:
    """
    bot.send_message(mensagem.chat.id, texto)


def rodar_bot():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Erro detectado no bot: {e}")
            time.sleep(5)


def rodar_flask():
    app.run(debug=False)

if __name__ == '__main__':
    bot_thread = threading.Thread(target=rodar_bot)
    flask_thread = threading.Thread(target=rodar_flask)

    bot_thread.start()
    flask_thread.start()
