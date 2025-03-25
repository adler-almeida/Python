'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''

import calendar

# Desafio
print ()
print ('='*53)
print ('                      DESAFIO 32')
print ('='*53)
print ()

# Realizando a pergunta ao usuário
ano = int(input('Qual ano você gostaria de saber se é Bissexto: '))

# Criando a condição com a importação calendar
print ()
if calendar.isleap (ano):
    print ('{} é Bissexto.'.format(ano))
else:
    print ('{} não é Bissexto.'.format(ano))

print ()
print ('='*53)