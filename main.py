import telebot

from bot_cliente import cadastro as cad
try:
    CHAVE_API = "5794347537:AAH8VbUo1TcFqZDBBbZugmb20JZ4NnTmItY"

    bot = telebot.TeleBot(CHAVE_API)

    user = {}

    @bot.message_handler(commands=["Agua 1L"])
    def pizza(mensagem):
        bot.send_message(mensagem.chat.id, "Qual a quantidade desejas?")

    @bot.message_handler(commands=["Agua 2L"])
    def hamburguer(mensagem):
        bot.send_message(mensagem.chat.id, "Pedido Recebido com Sucesso")

    @bot.message_handler(commands=["Galão de Agua"])
    def salada(mensagem):
        bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")

    @bot.message_handler(commands=["pedido"])
    def opcao2(mensagem):
        texto = """
        🤖 AguaoDelivery 🤖
    🤖 Venda de Agua 🤖
    ⏰ Horario:  24/7 ⏰
    
    ➖➖➖➖➖➖➖➖➖➖➖
    Produtos em estoque:
    Água 1 Litro         | R$2,00
    Água 2 Litro         | R$4,00
    Galão de Agua     | R$8,00
    ➖➖➖➖➖➖➖➖➖➖➖
    
    Entrega em todos os bairros da Grande São Luís.
    
    Taxa de Entrega R$ 5,00"""
        bot.send_message(mensagem.chat.id, texto)



    @bot.message_handler(commands=["cadastro"])
    def cadastro(mensagem):
        print(mensagem.text)

        bot.send_message(mensagem.chat.id, "Digite seu nome ex: /nome Nome Sobrenome")

    @bot.message_handler(commands=["nome"])
    def nome(mensagem):
        name = mensagem.text
        nome = name.replace("/nome ", '')
        user[f'{mensagem.chat.id}'].nome = nome

        bot.send_message(mensagem.chat.id, "Digite seu cpf agora ex: /cpf 99999999999")

        return nome

    @bot.message_handler(commands=["cpf"])
    def cpf(mensagem):
        cpf = mensagem.text
        cpf = cpf.replace("/cpf ", '')
        user[f'{mensagem.chat.id}'].cpf = cpf
        print(user[f'{mensagem.chat.id}'].nome, user[f'{mensagem.chat.id}'].cpf)
        bot.send_message(mensagem.chat.id, "Estamos quase lá. Digite seu telefone ex: /telefone 99999999999")

    @bot.message_handler(commands=["telefone"])
    def cpf(mensagem):
        telefone = mensagem.text
        print(telefone.replace("/telefone ", ''))
        telefone = telefone.replace("/telefone ", '')
        user[f'{mensagem.chat.id}'].telefone = telefone

        bot.send_message(mensagem.chat.id, "Para concluir o seu cadastro envie /cadastrar")

    @bot.message_handler(commands=["cadastrar"])
    def cadastrar(mensagem):

        usuario = user[f'{mensagem.chat.id}']
        print(usuario.nome, usuario.telefone, usuario.cpf)
        ca = cad(usuario.nome, usuario.cpf, usuario.telefone)
        print(ca)
        bot.send_message(mensagem.chat.id, f'{ca}')






    def verificar(mensagem):
        return True

    class User:
        def __init__(self, chat_id, nome, telefone, cpf):
            self.chat_id = chat_id
            self.nome = nome
            self.telefone = telefone
            self.cpf = cpf

    @bot.message_handler(func=verificar)
    def responder(mensagem):
        user["{0}".format(mensagem.chat.id)] = User(mensagem.chat.id, nome='', telefone='', cpf='')
        print(user)

        texto = """
        🤖 AguaoDelivery 🤖
    🤖 Bem-vindo(a) ao AguaoDelivery 🤖
    🤖 Venda de Agua 🤖
    ⏰ Horario:  24/7 ⏰
    
    ➖➖➖➖➖➖➖➖➖➖➖
    Serviços executados:
    
        - /cadastro Fazer o cadastro
        - /atualizar Pode atualizar informações cadastradas
        - /pedido Escolha o seu pedido
        - /status Acompanhe o status do seu pedido
    
    ➖➖➖➖➖➖➖➖➖➖➖
    
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
        bot.reply_to(mensagem, texto)

    @bot.message_handler()
    def responder_nome(mensagem):
        print(mensagem.text)
    bot.infinity_polling()
except:
    pass

