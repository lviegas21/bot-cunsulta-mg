
import re
import requests as rq




def cadastro( nome, cpf, telefone):
        if nome != '' and cpf != '' and telefone != '':
            val_cpf = validateCpf(cpf)
            val_telefone = validateTelefone(telefone)
            if val_cpf == False:
                return 'cpf incorreto!'
            if val_telefone == False:
                return 'Telefone Incorreto!'
            if val_cpf == True and val_telefone == True:
                rq.post('https://vcqtjk.deta.dev/api/cliente', json={
                    'nome': nome,
                    'cpf': cpf,
                    'telefone': telefone,
                    })
                return f'cadastro concluido. Bem vindo sr(a) {nome}'
        else:
            return 'Falta campos que nao estão preenchidos no seu cadastro!'

def validateCpf(cpf):


    # retirando pontos de maskara de cpf se existir
    cpf.replace('.', '')

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

def validateTelefone(telefone):
    padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
    resposta = re.findall(padrao, telefone)
    if resposta:
        return True
    else:
        return False