#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

print ()
print ('======== DESAFIO 006 ========')
print ()
print ('Crie um algoritmo que leia um numero e mostre o seu dobro,\ntriplo e raiz quadrada.')
print ()
print ('=============================')
print ()

numero = int(input('Informe um número: '))


dobro = numero * 2
triplo = numero * 3
raiz4 = numero ** 0.5

print ('==============================')
print ('O dobro de {} é {}.'.format(numero,dobro))
print ('O triplo de {} é {}.'.format(numero,triplo))
print ('A raiz quadrada de {} é {:.2f}.'.format(numero,raiz4))   #:.nf de flutuante, para pegar as 2 casas após a virgula
print ('==============================')


