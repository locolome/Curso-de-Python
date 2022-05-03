ca=float(input('Quantas camisas serão compradas?'))
vl=float(input('Qual o valor das camisas?'))
if ca<=5:
    des=vl-(vl*0.03)
    print('O valor final a ser cobrado será de R${:.2f}.'.format(des))
if ca>5 and ca<=10:
    des=vl-(vl*0.05)
    print('O valor final a ser cobrado será de R${:.2f}.'.format(des))
if ca>10:
    des=vl-(vl*0.10)
    print('O valor final a ser cobrado será de R${:.2f}.'.format(des))