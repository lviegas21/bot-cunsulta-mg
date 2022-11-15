import requests as rq

class Pedido:
    def __init__(self, chat_id, quantidade, id_produto):
        self.chat_id = chat_id
        self.quantidade = quantidade
        self.id_produto = id_produto

def pedido_fechado():


    rq.post('https://vcqtjk.deta.dev/api/cliente', json={
            'nome': nome,
            'cpf': cpf,
            'telefone': telefone,
    })
    return f'cadastro concluido. Bem vindo sr(a) {nome}'