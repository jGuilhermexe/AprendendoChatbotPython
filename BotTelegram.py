import telebot
from database import salvar_mensagem
CHAVE_API = "7710595076:AAFHY0YGmgKIMDJ1c-4-IUuHcRg7X7jNiaI"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["AuxilioMoradia"])
def AuxilioMoradia(mensagem):
    bot.send_message(mensagem.chat.id, "O auxílio moradia é uma bolsa que todos os estudantes que atinjam os requisitos minimos")

@bot.message_handler(commands=["PEnoCampus"])
def PEnoCampus(mensagem):
    pass

@bot.message_handler(commands=["AuxiliosUFRPE"])
def AuxiliosUFRPE(mensagem):
    pass


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Certo, você necessita de ajuda no quesito "Bolsas e Auxílios"
Selecione um tópico que seja de seu interesse (Clique no item):
    /AuxilioMoradia
    /PEnoCampus
    /AuxiliosUFRPE
Responder qualquer outra coisa não irá funcionar, por favor, clique em uma das opções:
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    pass


usuarios_desabafo = {}


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    usuarios_desabafo[mensagem.chat.id] = True  
    bot.send_message(mensagem.chat.id, "Sinta-se à vontade para desabafar. Estou aqui para ouvir. ❤️\n\nDigite sua mensagem:")


@bot.message_handler(func=lambda mensagem: mensagem.chat.id in usuarios_desabafo)
def desabafo(mensagem):
    salvar_mensagem(mensagem.chat.id, mensagem.from_user.first_name, mensagem.text)  # Salva no MySQL
    bot.send_message(mensagem.chat.id, "Eu recebi sua mensagem. Se precisar continuar desabafando, estou aqui. 💙")

    print(mensagem)

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Seja bem-vindo ao Bot AtendiNAPS - UABJ!
Selecione um tópico que seja de seu interesse (Clique no item):
    /opcao1 Dúvidas relacionadas a Bolsas
    /opcao2 Dúvidas relacionadas a Universidade
    /opcao3 Gostaria de desabafar
Responder qualquer outra coisa não irá funcionar, por favor, clique em uma das opções:

    """
    bot.reply_to(mensagem, texto)


bot.polling()