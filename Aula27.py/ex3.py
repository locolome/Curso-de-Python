'''def leiaint():
    a=input('Digite um n: ')
    if a.isnumeric()==True:
       print('é inteiro')
    else:
        print('Não é inteiro.')
leiaint()'''

def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=input(msg)
        if (n.isnumeric()):
            valor=int(n)
            ok=True
        else:
            print('Digite um número válido!')
        if ok:
            break
    return valor

n=leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')