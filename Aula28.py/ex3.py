from MinhasFuncoes import *

linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de linhas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))
a=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
b=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)

if len(a)==len(b) and len(a[0])==len(b[0]):
    print(f'Matriz A={a} \nMatriz B: {b} \nMatriz C (A+B) = {soma_matrizes(a,b)}')
else:
    print('As matrizes não tem a mesma ordem.')















