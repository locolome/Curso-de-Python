from code import InteractiveInterpreter


while True:
    n=int(input('Digite um valor: '))
    if n>0:
        for c in range(0,11):
            tab=c*n
            print(tab)
    if n<0:
        print('Encerrando...')
        break