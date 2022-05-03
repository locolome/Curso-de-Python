ca=float(input('Qual o cargo do funcionário? Digite: 1 para programador de sistemas\n 2 para analista de sistemas \n 3 para analsita de banco de dados.\n'))
sa=float(input('Digite o salário do funcionário: '))
if ca==1 or ca==2 or ca==3:
    if ca==1:
        pro=sa+(sa*0.3)
        print('O novo salário será de R${}.'.format(pro))
    if ca==2:
        pro=sa+(sa*0.2)
        print('O novo salário será de R${}.'.format(pro))
    if ca==3:
        pro=sa+(sa*0.15)
        print('O novo salário será de R${}.'.format(pro))
else:
    print('Opção inválida.')
        
