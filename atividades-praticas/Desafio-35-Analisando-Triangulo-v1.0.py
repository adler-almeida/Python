'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

# Desafio
print ()
print ('='*53)
print ('                      DESAFIO 35')
print ('='*53)
print ()

# Enunciado
print ('Informe tres retas que iremos dizer\nse elas formam ou não um triângulo.')

# Solicitando e armazenando dados.
print ()
valor1 = int(input('Informe o primeiro comprimento: '))
valor2 = int(input('Infomre o segundo comprimento: '))
valor3 = int(input('Informe o terceiro comprimento: '))

# Criando Lista
lista = [valor1,valor2,valor3]
a, b, c = lista

# Criando a condição e formula
print ()
if a + b > c and a + c > b and b + c > a:
    print ('Os comprimentos formam um triângulo.')
else:
    print ('Os comprimentos não formam um triângulo.')
print ()
print ('='*53)