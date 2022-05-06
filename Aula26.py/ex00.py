def exibirMensagem():#declarando uma função
    print('Python é fácil')

exibirMensagem()#executa a função, sem isso não é executada

#variavel não definida
def exibirMensagemBoasVindas(pessoa,mensagem):
    print(f'{mensagem}, {pessoa} ')

exibirMensagemBoasVindas('Janaína', 'Bem vinda')

#variável definida
def exibirMensagemBoasVindas(pessoa='fulano',mensagem='Bem vindo'):
    print(f'{mensagem}, {pessoa} ')

exibirMensagemBoasVindas()