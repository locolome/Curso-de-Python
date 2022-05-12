from MinhasFuncoes import *

linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de linhas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))
m1=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
constante=int(input('Informe a constante que multiplicará a matriz gerada: '))
print(f'Matriz gerada: {m1} \nMatriz C (M * Constante)= {multiplica_matriz_por_consatante(m1,constante)}')
