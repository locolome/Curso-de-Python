from re import I


'''ano=int(input('Qual o ano de nascimento do atleta? '))
i=2022-ano
if i<=9:
    print('O atleta está na categoria: MIRIM.')
if i<=14 and i>9:
    print('O atleta está na categoria INFANTIL.')
if i<=19 and i>14:
    print('O atleta está na categoria JUNIOR.')
if i<=25 and i>19:
    print('O atleta está na categoria SÊNIOR')
if i>25:
    print('O atleta está na categoria MAS
    TER')'''

from datetime import date

atual=date.today().year
nascimento=int(input('Ano de nascimento: '))
idade= atual-nascimento
print('O atleta tem {} anos.'.format(idade))

if idade <=9:
    print('Classificação: mirim')
elif idade <=14:
    print('Classificação: infantil')
elif idade <=19:
    print('Classificação junior')
elif idade <=25:
    print('Classificação: sênior')
elif idade > 25:
    print('Classificação: master')