'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
calcule e mostre o comprimento da hipotenusa.
**Importando modulo.**
'''

#Pode ser feito também usando a formula de Teorema de Pitágoras (c² = a² + b²), a e b são catetos, c é a hipotenusa.

from math import hypot, ceil
#Hypot é para calcular hipotenusa, ceil é para arredondar para o teto, ou seja, para cima.

print ()
print ('='*43)
print ('                 DESAFIO 17')
print ('='*43)
print ()

catetoa = float(input('Informe o Cateto A: '))
catetob = float(input('Informe o Cateto B: '))
hipotenusa = hypot(catetoa,catetob)

print ()
print ('A Hipotenusa mede: {}.'.format(ceil(hipotenusa)))
print ()
print ('='*43)
