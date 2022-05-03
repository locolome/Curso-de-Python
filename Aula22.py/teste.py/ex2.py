tupla=('santos','chapecoense','atlético mineiro','corinthians','cuiabá','internacional','avaí','bragantino','palmeiras','coritiba','flamengo','são paulo','botafogo','fluminense','américa','ceará','athletico','goiás','juventude','fortaleza')
a=tupla[:5]
b=tupla[-4:]
c=sorted(tupla)

print(f'Os 5 primeiros colocados são: {a}')
print(f'Os 4 ultimos colocados são: {b}')
print(f'Os times em ordem alfabética são: {c}')

for index,time in enumerate(tupla):
    if time=='chapecoense':
        print(f'Chapecoense está na {index+1}ª posição.')
