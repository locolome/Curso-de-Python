from re import T


print('\033[36m-#\033[m'*16)
print('Seja bem vindo ao nosso banco!')
print('\033[36m-#\033[m'*16)


valor=int(input('Qual será o valor a ser sacado?'))
total=valor
ced=50
totced=0
while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'Total de {totced} cédulas de R${ced}. ')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totced=0     
        if total==0:
            break

