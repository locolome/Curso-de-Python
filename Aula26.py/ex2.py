def escreva(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)

#programa principal
'''escreva('Na aula de hoje estudamos funções em Python')
escreva('Turma Inf 9 - SENAC - SCS')'''
#leitura do usuario
escreva(input('Digite uma frase: '))