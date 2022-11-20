from app_base import app
from pyrogram import Client, filters
import re
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
)
from utils.constants import produto_1, produto_2, produto_3, produto_4
from app_base import app, user, pedido
from controllers.bot_pedido import pedido_fechado

@app.on_message(filters.command('pedidos'))
async def pedidos(client, message):
    await message.reply(
        """
        🤖 AguaoDelivery 🤖
    🤖 Venda de Agua 🤖
    ⏰ Horario:  24/7 ⏰

    ➖➖➖➖➖➖➖➖➖➖➖
    Produtos em estoque:
    1 Água 500ml           | R$2,00
    2 Água 1 Litro         | R$3,50
    3 Água 2 Litro         | R$5,00
    4 Galão de Agua        | R$10,00
    ➖➖➖➖➖➖➖➖➖➖➖

    Entrega em todos os bairros da Grande São Luís.

    Taxa de Entrega R$ 5,00""",
        reply_markup=ReplyKeyboardMarkup(
            [
                ['1', '2', '3', '4'],

            ],
            resize_keyboard=True
        ),
    )

    global isPedido
    isPedido = True
    print(isPedido)


@app.on_message(filters.regex("([0-9])"))
async def escolhas(client, message):
    global isPedido
    global isQuantidade
    if isPedido == False:
        padrao = '([0-9])'

        if isQuantidade == True:
            print('entrei')
            resposta = re.findall(padrao, message.text)
            print(resposta)
            pedido[f'{message.chat.id}'].quantidade = message.text


            return await fechando_carrinho(client, message)
        else:
            return await pedidos(client, message)


    else:
        isPedido = False
        isQuantidade = True
        if int(message.text) == 1:
            return await pedido_one(client, message)
        elif int(message.text) == 2:
            return await pedido_two(client, message)
        elif int(message.text) == 3:
            return await pedido_three(client, message)
        elif int(message.text) == 4:
            return await pedido_three(client, message)
        else:
            await message.reply('Numero Invalido! Escolha Novamente')
            return await pedidos(client, message)


@app.on_message(filters.regex("1"))
async def pedido_one(client, message):
    print('oi')
    global isPedido
    global isQuantidade

    isPedido = False

    pedido[f'{message.chat.id}'].id_produto = '1'
    await message.reply(
        'Digite a quantidade Agua de 500ml',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['1', '2', '3', '4', '5', '6', '7'],
                ['8', '9', '10', '20', '30', '40'],

            ],
            resize_keyboard=True
        ),
    )
    isQuantidade = True


@app.on_message(filters.regex('2'))
async def pedido_two(client, message):
    numero = message.text
    pedido[f'{message.chat.id}'].id_produto = '2'
    await message.reply(
        'Digite a quantidade de Agua de 1 Litro',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['1', '2', '3', '4', '5', '6', '7'],
                ['8', '9', '10', '20', '30', '40'],

            ],
            resize_keyboard=True
        ),
    )


@app.on_message(filters.regex('3'))
async def pedido_three(client, message):
    pedido[f'{message.chat.id}'].id_produto = '3'
    await message.reply(
        'Digite a quantidade de Agua de 2 Litro',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['1', '2', '3', '4', '5', '6', '7'],
                ['8', '9', '10', '20', '30', '40'],

            ],
            resize_keyboard=True
        ),
    )

@app.on_message(filters.regex('3'))
async def pedido_four(client, message):
    pedido[f'{message.chat.id}'].id_produto = '3'
    await message.reply(
        'Digite a quantidade de galões de agua',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['1', '2', '3', '4', '5', '6', '7'],
                ['8', '9', '10', '20', '30', '40'],

            ],
            resize_keyboard=True
        ),
    )


@app.on_message(filters.regex('3'))
async def fechando_carrinho(client, message):
    nome = pedido[f'{message.chat.id}'].id_produto
    produto = pedido[f'{message.chat.id}'].id_produto
    qtd = pedido[f'{message.chat.id}'].quantidade

    if int(produto) == 1:
        produto = 2
    elif int(produto) == 2:
        produto = 3.5
    elif int(produto) == 3:
        produto = 5
    else:
        produto = 10
    print(produto, qtd)
    resultado = produto * int(qtd)

    pedido[f'{message.chat.id}'].total = resultado

    await message.reply(
        f"""
Deseja encerrar seus pedidos?
{produto_1 if nome == 1 else ""}
{produto_2 if nome == 2 else ""}
{produto_3 if nome == 3 else ""}
{produto_4 if nome == 3 else ""}
Valor Total {resultado} $
Digite (S) para encerrar seus pedidos e (N) para ir ao Menu""", reply_markup=ReplyKeyboardMarkup(
            [
                ['S', 'N']

            ],
            resize_keyboard=True
        ),
    )

@app.on_message(filters.regex('S'))
async def anotando_pedido(client, message):
    ped = pedido[f'{message.chat.id}']
    msg = await pedido_fechado(ped)
    await message.reply(f'{msg}')




