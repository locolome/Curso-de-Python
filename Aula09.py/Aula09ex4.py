ano=int(input('Qual seu ano de nascimento?'))
i=2022-ano
if i<18:
    print('Você ainda irá se alistar.')
    fa=18-i
    print('Falta {} anos até o alistamento militar.'.format(fa))
if i>18:
    print('Já passou do tempo de alistamento.')
    pa=i-18
    print('Passaram {} anos desde o prazo do alistamento.'.format(pa))
if i==18:
    print('Está na hora de se alistar.')




