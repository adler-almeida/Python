"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza
"""

print ()
print ('='*43)
print ('                  DESAFIO 27')
print ('='*43)
print ()

nome = str(input ('Nome completo: '))
nome = nome.split()

print ('Primeiro: {}'.format(nome[0]))
print ('Ultimo: {}'.format(nome[-1]))
print ()
print ('='*43)