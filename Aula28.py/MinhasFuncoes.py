#ex1
from random import randrange


def calcular_area_circulo(raio,pi=3.14):
    return pi*(raio**2)

def calcular_area_triangulo(b,h):
    return (b*h)/2

def calcular_area_retangulo(b,h):
    return b*h

#ex2
def gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final):
    from random import randrange
    m=[[randrange(intervalo_inicial, intervalo_final) for i in range(colunas)] for j in range(linhas)]
    return m

def calcula_traco_da_matriz(matriz):
    traco=[]
    soma=0
    for i in range(len(matriz)):
        traco.append(matriz[i][soma])
        soma+=1
    return sum(traco)


#ex3
def soma_matrizes(a,b):
    '''c=[]
    a=[[randrange(1,11) for i in range(3)] for j in range (3)]
    b=[[randrange(1,11) for i in range(3)] for j in range (3)]
    for i in range(3):
        for j in range(3):
            soma=a[i][j]+b[i][j]
            c.append(soma)
    for i in range(len(c)):
        for j in range(len(c)):
            print(c[i][j], end=' ')
        print()'''
    c=[]
    for i in range(len(a)):
        c.append([])#tem que usar pra virar matriz, termina de ler uma coluna ou linha e começa outra
        for j in range(len(a[i])):
            c[i].append(a[i][j]+b[i][j])
        return c


#ex4

def multiplica_matriz_por_consatante(matriz,constante):
    m=[]
    for i in range(len(matriz)):
        m.append([])
        for j in matriz[i]:
            m[i].append(j*constante)
    return m 
    
#ex5
def obtem_dados_funcionarios():
    '''l=['Marcos','M','Janaína','F','Paulo','M','Alexandre','M','Marta','F','Lorenzo','M','Jenifer','F']
    return l'''
    func=[['Ana','F'],['Mateus','M'],['Emilio','M'],['Beatriz','F'],['Carla','F'],["Fernando",'M']]
    return func

def retorna_num_hom_mul(matriz):
    h=m=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for nome,dados in matriz:
        print(nome, dados)

    for i in range(linha):
        if matriz[i][j]=='F':
            m+=1
        else:
            h+=1
    return f'\nQuantidade de mulheres cadastradas: {m} \nQuantidade de homens cadastrados: {h}'
