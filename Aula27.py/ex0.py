def escreve(msg):
    """
    print de mensagem informada pelo usuario
    msg: entrada do usuário para programa
    """
    #criar a doumentação de uma função para ser usada no help
    print('~')
    print(msg)
    print('~')

escreve(input('Digite uma frase: '))

help(escreve)

def teste(b):
    b+=4 #variavel de escopo local
    c=2 #variavel de escopo local
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')

a=5#variavel de escopo global
teste(a)
print(f'A fora da função vale {a}')
#print(f'B dentro da função vale {b}')
#print(f'C dentro da função vale {c}')


