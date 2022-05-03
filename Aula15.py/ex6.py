
'''var=0
var1=0

while True:
    cod=int(input('Informe o código do cargo de um funcionário:\n 1 para Enfermeiro \n 2 para Nutricionista \n 3 para Médico \n  '))
    sal=float(input('Informe o salário do funcionário: ')) 
    if cod==0:
        break
    if cod==2:
        var+=sal 
        var1+=1
media=var/var1
print('A média salárial dos nutricionistas é de {}. '.format(media))'''

print('Código de cargo: \n1 : Enfermeiro \n2 : Nutricionista \n3 : Médico(a)')
qtdenutri=0
totalsalnutri=0
while True:
    cargo=int(input('Informe um código do cargo: '))
    if cargo>=1 and cargo<=3:
        sal=float(input('Salário R$: '))
        if cargo==2:
            qtdenutri+=1
            totalsalnutri+=sal
        resp=input('Deseja continuar: [S/N]')
        if resp.upper()=="N":
            break
    else:
        print('Código invalido.')

if qtdenutri>0:
    media=totalsalnutri/qtdenutri
    print(f'Média salarial das nutricionistas R$: {media:.2f}')
else:
    print('Não foram inseridos dados sobre as nutricionistas.')

        


    