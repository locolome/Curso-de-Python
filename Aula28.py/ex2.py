
from MinhasFuncoes import gera_matriz_aleatoria
from MinhasFuncoes import calcula_traco_da_matriz
linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de linhas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))

m=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
print(f'Matriz gerada: {m}')
if len(m)==len(m[0]):
    print(f'Traço da matriz gerada: {calcula_traco_da_matriz(m)}')
else:
    print('Não é possível calcular o traço pois não é uma função quadrada.')
