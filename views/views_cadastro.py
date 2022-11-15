
from controllers.bot_cliente import User, cadastro as cad
from pyrogram import Client, filters

from app_base import app, user, pedido


@app.on_message(filters.command('cadastro'))
async def callbacks(client, message):
    resize_keyboard=True
    await message.reply('Digite seu nome ex: /nome Nome Sobrenome')

@app.on_message(filters.command('nome'))
async def callbacks(client, message):
    name = message.text
    nome = name.replace("/nome ", '')
    user[f'{message.chat.id}'].nome = nome
    resize_keyboard=True
    await message.reply('Digite seu cpf ex: /cpf 99999999999')

@app.on_message(filters.command('cpf'))
async def callbacks(client, message):
    resize_keyboard=True
    cpf = message.text
    cpf = cpf.replace("/cpf ", '')
    user[f'{message.chat.id}'].cpf = cpf
    print(user[f'{message.chat.id}'].nome, user[f'{message.chat.id}'].cpf)
    await message.reply('Digite seu telefone ex: /telefone 99999999999')

@app.on_message(filters.command('telefone'))
async def callbacks(client, message):
    resize_keyboard=True
    telefone = message.text
    telefone = telefone.replace("/telefone ", '')
    user[f'{message.chat.id}'].telefone = telefone
    print(user[f'{message.chat.id}'].nome, user[f'{message.chat.id}'].cpf)
    await message.reply('Para concluir seu cadastro. Digite /cadastrar')

@app.on_message(filters.command('cadastrar'))
async def callbacks(client, message):
    resize_keyboard=True
    usuario = user[f'{message.chat.id}']
    print(usuario.nome, usuario.telefone, usuario.cpf)
    ca = cad(usuario.nome, usuario.cpf, usuario.telefone)
    print(ca)
    await message.reply(f'{ca}')