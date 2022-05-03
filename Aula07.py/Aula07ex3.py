

sa=float(input('Qual o salário de um funcionário?'))
if sa>1250:
    ma=sa *0.15
    print('O valor do aumento do salário {} é de {}.'.format(sa,ma))
else:
    me=sa *0.10
    print('O valor do aumento do salário {:.2f} é de {:.2f}.'.format(sa,me))
