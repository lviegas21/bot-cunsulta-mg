import requests as rq




def cadastro( nome, cpf, telefone):
        if nome != '' and cpf != '' and telefone != '':
            rq.post('https://vcqtjk.deta.dev/api/cliente', json={
                'nome': nome,
                'cpf': cpf,
                'telefone': telefone,
})