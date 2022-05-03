'''senha=123456
nome=input('Digite seu nome: ')
inp=int(input('Digite sua senha: '))

if inp==senha:
    print('Olá, {}. Seja bem vindo ao nosso banco!'.format(nome))
if inp!=senha:
    inp1=int(input('Senha incorreta! Você ainda têm 2 tentativas.'))
    if inp1!=senha:
        inp2=int(input('Senha incorreta! Você ainda têm 1 tentativa.'))
        if inp2!=senha:
            print('Sua senha foi bloqueada! Por favor dirija-se a um de nossos caixas.')'''
from re import I


for c in range(3,0,-1):
    senha=int(input('Senha: '))
    if senha == 123456:
        print('Olá, você. Seja bem vindo ao nosso banco!')
        break
    elif senha!=123456:
        print('Senha incorreta! Você ainda tem {} tentativas.'.format(c-1))
        if c==1:
            print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')
            break