menu=int(input('*********************************\n CÁLCULO DE GRANDEZAS ELÉTRICAS \n********************************\n 1.Tensão(em volt)\n 2.Resitência \n 3. Corrente(em Amperé)\n *********************************** \n Qual grandeza deseja calcular?'))
if menu==1:
    re=float(input('Informe o valor da resistência: '))
    co=float(input('Informe o valor da corrente: '))
    te=re*co
    print('A tensão vale {} volts.'.format(te))
if menu==2:
    te=float(input('Informe o valor da tensão: '))
    co=float(input('Informe o valor da corrente: '))
    re=te/co
    print('A resistência vale {} ohm.'.format(re))
if menu==3:
    re=float(input('Informe o valor da resistência: '))
    te=float(input('Informe o valor da tensão: '))
    co=te/re
    print('A corrente vale {} amperés'.format(co))
