from random import randint
from re import A
n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados são: ', end=' ')

for num in n:
    print(f'{num}', end =' ')

print(f'\nO maior valor sorteado foi {max(n)}.')
print(f'\nO menor número sorteado é {min(n)}.')
