print('## Programa de emprétimo ## \n Responda: 0 - Não e 1- Sim')
nomeneg=int(input('Possui nome negativado?'))

if nomeneg == 1:
    print('Não pode realizar o empréstimo.')
else:
    cartass=int(input('Possui carteira assinada?'))
    if cartass == 0:
        print('Não pode realizar o empréstimo.')
    else:
            possuicp=int(input('Possui casa própria?'))
            if possuicp == 0:
                print('Não pode realizar o empréstimo')
            else:
                print('Concede o empréstimo.')
