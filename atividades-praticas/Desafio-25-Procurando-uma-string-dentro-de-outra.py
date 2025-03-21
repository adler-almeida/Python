"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

print ()
print ('='*43)
print ('                  DESAFIO 25')
print ('='*43)
print ()

palavradecomparacao = 'SILVA'

nometodo = str(input('Nome completo: '))
nometodo = nometodo.upper().split()
print ()

if palavradecomparacao in nometodo:    # comparação se, senão. if, else.
    print ('Parabébs, seu nome tem "Silva" no nome.')
else:
    print ('Infelizmente seu nome não tem "Silva".')
print ()
print ('='*43)
