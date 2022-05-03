'''ci=input('Digite o nome de uma cidade: ')
sp=ci.find('Santa')
if sp== 0:
    print('A cidade começa com o nome Santa.')
else:
    print('A cidade não começa com o nome Santa.')'''

ci=input('Digite o nome de uma cidade: ').strip()

print(ci[:5].upper()=='SANTA')

