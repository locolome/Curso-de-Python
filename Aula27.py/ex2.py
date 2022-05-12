


def ficha(nome='lorenzo',gols='69'):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato. ')

#programa principal
n=input('Nome do jogador: ')
g=input('Número de gols: ')

if g.isnumeric():
    g=int(g)#forçando g a ser int
else: 
    g=0
if n.strip()=='':
    ficha(gols=g)
else:
    ficha(n,g)

'''if type(n)==int:
    print('Sim')
else:
    print('Não')'''

