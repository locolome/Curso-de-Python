num=int(input('Digite um número inteiro:'))
esc=int(input('Qual será a base de conversão: 1) para binário, 2) octal, 3)hexadecimal: '))
if esc==1:
    bina=bin(num)
    print('O número {} convertido para binário é {}.'.format(num,bina))
else:
    if esc==2:
        octa=oct(num)
        print('O número {} convertido para octal é {}.'.format(num,octa))
    else:
        if esc==3:
            hexa=hex(num)
            print('O número {} convertido para hexadecimal é {}.'.format(num,hexa))




