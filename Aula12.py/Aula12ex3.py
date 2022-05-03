es1=float(input('Digite a estatura da pessoa 1: '))
es2=float(input('Digite a estatura da pessoa 2: '))
es3=float(input('Digite a estatura da pessoa 3: '))

if es1>es2 and es2>es3:
     print('As estaturas em ordem decrescente são: {:.2f}, {:.2f} e {:.2f}.'.format(es1,es2,es3))
if es1>es3 and es3>es2:
     print('As estaturas em ordem decrescente são: {:.2f}, {:.2f} e {:.2f}.'.format(es1,es3,es2))
if es2>es3 and es3>es1:
     print('As estaturas em ordem decrescente são: {:.2f}, {:.2f} e {:.2f}.'.format(es2,es3,es1))
if es2>es1 and es1>es3:
     print('As estaturas em ordem decrescente são: {:.2f}, {:.2f} e {:.2f}.'.format(es2,es1,es3))
if es3>es2 and es2>es1:
     print('As estaturas em ordem decrescente são: {:.2f}, {:.2f} e {:.2f}.'.format(es3,es2,es1))
if es3>es1 and es1>es2:
     print('As estaturas em ordem decrescente são: {:.2f}, {:.2f} e {:.2f}.'.format(es3,es1,es2))