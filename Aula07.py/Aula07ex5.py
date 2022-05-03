a=float(input('Digite um número a:'))
b=float(input('Digite um número b diferente de a:'))
menu=int(input('Escolha uma das opção a seguir e a digite;1.média ponderada,2.quadrado da soma,3.cubo do menor número:'))
if menu>4 and menu<0:
    print('Opção inválida.')
else:    
    if menu== 2:
        qua=(a+b)**2
        print('O quadrado da soma de {} e {} vale {}.'.format(a,b,qua))
    else:
        if menu==3:   
            if a>b:
                cub=(b**3)
                print('O cubo do menor número é {}.'.format(cub))
            else: 
                cua=(a**3)
                print('O cubo do menor número é {}.'.format(cua))
        else: 
                    
            if menu==1:
            
                me=(2*a)+(3*b)/(2+3)
                print('A média ponderada vale {}.'.format(me))
                