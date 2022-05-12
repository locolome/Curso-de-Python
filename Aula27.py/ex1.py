
'''def voto(ano):
    if ano<=2006 and ano>=2004:
        print('Voto OPCIONAL.')
    elif ano<2004:
        print('Voto OBRIGATÓRIO.')
    elif ano>2006:
        print('Voto NEGADO.')
ano=int(input('Digite sua data de nascimento: '))
voto(ano)'''

def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano

    if idade<16:
        return f'Com {idade} anos: não vota.'
    elif idade<18 and idade>65:
        return f'Com {idade} anos: voto opcional.'
    else:
        return f'Com {idade} anos: voto obrigatório.'

#programa principal
nasc=int (input('Em que ano você nasceu? '))
print(voto(nasc))