import requests as rq
from app_base import user

class Pedido:
    def __init__(self, chat_id, quantidade, id_produto, total):
        self.chat_id = chat_id
        self.quantidade = quantidade
        self.id_produto = id_produto
        self.total = total

async def estoque(ped):
    estoque = rq.get(f'https://vcqtjk.deta.dev/api/estoque/{ped.id_produto}')
    qtd_est = estoque.json()
    print(qtd_est)
    return qtd_est['quantidade']


async def isClient(ped):
    return user[f'{ped.chat_id}'].cpf

async def AdicionarEntrega(ped):
    cliente = rq.get(f'https://vcqtjk.deta.dev/api/cliente/all')
    client = cliente.json()
    for val in client:
        if val['cpf'] == user[f'{ped.chat_id}'].cpf:

            rq.post('htps://vcqtjk.deta.dev/api/entrega', json={
                'status': 'processamento',
                'fk_pedido': val['id'],
            })

async def salvaPedido(ped):
    cliente = rq.get(f'https://vcqtjk.deta.dev/api/cliente/all')
    client = cliente.json()
    for val in client:
        if val['cpf'] == user[f'{ped.chat_id}'].cpf:
            endereco = rq.get(f'https://vcqtjk.deta.dev/api/endereco/{val["id"]}').json()
            print(endereco)
            pedido = rq.post(f'https://vcqtjk.deta.dev/api/pedido', json={
                'quantidade': ped.quantidade,
                'total': ped.total,
                'fk_cliente': val['id'],
                'fk_endereco': endereco['id'],
                'fk_produto': ped.id_produto
            })
            entrega = AdicionarEntrega(ped)
            return f'Recebemos seu pedido sr(a) {val["nome"]}. Será enviado para ' \
                   f'Rua: {endereco["rua"]} numero: {endereco["numero"]}\n' \
                   f'Bairro: {endereco["bairro"]} cep: {endereco["cep"]}\n' \
                   f'Caso deseje atualizar ou informar outro acesse /endereco'
    return f'sr(a) não está cadastrado ainda no nosso sistema. Faço o cadastro acessando o /cadastro'


async def pedido_fechado(ped):


    qtd_estoque = await estoque(ped)
    isCliente = await isClient(ped)
    print('aq' + isCliente)

    if int(qtd_estoque) > ped.total:
        return f'Não temos em estoque a quantidade desejada. Só temos {int(qtd_estoque)}'
    if isCliente == None or isCliente == '':

        return f'Se já tem cadastro no aguao delivery é só botar o /cpf xxxxxxxxxxxxx com o seu cpf e tentar ' \
               f'novamente fazer o pedido. Senão tiver cadastro faça logo seu cadastro, seu pedido está salvo!'
    if isCliente != None:
        return await salvaPedido(ped)
