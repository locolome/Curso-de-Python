'''while True:
    a=input('\033[4;35;42mDigite o comado ou "Fim" para encerrar:\033[m ')
    if a=='help':
        help()
    if a=='Fim':
        break'''
c=('\033[m','\033[0.30;41','\033[0;30;42m','\033[0;30;43m','\033[0;30;44m','\033[0;30;45m','\033[0;30;46m')
def ajuda(com):
    titulo(f'Acessando o manual de comandos {com}',4)
    print(c[6],end=' ')
    help(com)
    print(c[0],end=' ')

def titulo(msg,cor=0):
    tam=len(msg)+4
    print(c[cor],end=' ')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0],end=' ')

comando=''
while True:
    titulo('Ajuda python',2)
    comando=input("Função da Biblioteca: ")
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
