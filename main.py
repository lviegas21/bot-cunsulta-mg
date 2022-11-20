from app_base import app, user, pedido
from pyrogram.handlers import MessageHandler

from controllers.bot_cliente import User
from controllers.bot_pedido import Pedido
from views.views_cadastro import callbacks
from views.view_pedido import pedidos, pedido_one, pedido_two, pedido_three, escolhas, fechando_carrinho, anotando_pedido
from pyrogram import Client, filters
import re
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
)

@app.on_message(filters.command('help') |filters.command('start'))
async def start_command(client, message):
    user["{0}".format(message.chat.id)] = User(message.chat.id, nome='', telefone='', cpf='')
    pedido["{0}".format(message.chat.id)] = Pedido(chat_id=message.chat.id, quantidade='', id_produto='', total='')
    await message.reply(
        'Esse é o menu para pedir ajuda!\n'
        'Use **/start** para iniciar o bot!\n'
        'Use **/menu** para esse menu em teclado!\n'
        'Use **/comandos** para saber o que é possivel fazer!\n'
        'Use **/pedidos** para fazer seu pedido!\n'
        'Use **/teclado** para ver um teclado de comandos\n'
        'Use **/dev** para ver por quem foi desenvolvido\n'


    )

@app.on_message(filters.command('dev'))
async def dev(client, message):

    await message.reply('Desenvolvido por **Lucas Viegas**')

@app.on_message()
async def hello(client, message):

    await message.reply('Desculpe! Não Entendi')



app.add_handler(MessageHandler(start_command))
app.add_handler(MessageHandler(dev))
app.add_handler(MessageHandler(callbacks))
app.add_handler(MessageHandler(pedidos))
app.add_handler(MessageHandler(escolhas))

app.add_handler(MessageHandler(pedido_one))
app.add_handler(MessageHandler(pedido_two))
app.add_handler(MessageHandler(pedido_three))
app.add_handler(MessageHandler(fechando_carrinho))
app.add_handler(MessageHandler(anotando_pedido))

app.run()