pr=float(input('Qual é o preço do produto? '))
mp=float(input('Digite o método de pagamento:\n 1 para à vista dinheiro/cheque.\n 2 para à vista no cartão de desconto. \n 3 para em até 2x no cartão:preço normal.\n'))
if mp==1:
    des=pr-(pr*0.10)
    print('O valor a ser pago pelo produto será de R${}.'.format(des))
if mp==2:
    des=pr-(pr*0.05)
    print('O valor a ser pago pelo produto será de R${}.'.format(des))
if mp==3:
    des=pr
    print('O valor a ser pago pelo produto será de R${}.'.format(des))
