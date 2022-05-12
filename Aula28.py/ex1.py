from MinhasFuncoes import *
op=int(input('1.Círculo \n2.Triângulo \n3.Retângulo \nQual figura deseja calcular a área? '))

if op<1 or op>3:
    print('Opção ínvalida')
elif op==1:
    raio=int(input('Digite o raio do círculo: '))
    a=calcular_area_circulo(raio)
    print(f'A área do círculo é {a}.')
elif op==2:
    b=int(input('Digite a base do triângulo: '))
    h=int(input('Digite a altura do triângulo: '))
    a=calcular_area_triangulo(b,h)
    print(f'A área do triângulo é {a}.')
elif op==3:
    b=int(input('Digite a base do retângulo: '))
    h=int(input('Digite a altura do retângulo: '))
    a=calcular_area_retangulo(b,h)
    print(f'A áre do retângulo é {a}.')
