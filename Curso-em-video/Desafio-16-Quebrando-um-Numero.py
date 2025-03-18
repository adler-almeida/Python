"""
Crie um programa que leia um número qualquer pelo teclado, e mostre na tela, a sua porção inteira.
Ex: 6.127, parte inteira 6.
importando modulos.
"""
from math import trunc
#Importei (de, matematica, importar, números antes da vírgula = form math import trunc

print ()
print ('='*43)
print ('                 DESAFIO 16')
print ('='*43)
print ()

ndecimal = float(input('Digite um numero decimal: '))
ninteiro = trunc(ndecimal)

print ()
print ('Número informado: {}. \nParte inteira é: {}.'.format(ndecimal,ninteiro))
print ()
print ('='*43)

