'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
# Desafio5
print ()
print ('='*43)
print ('                  DESAFIO 30')
print ('='*43)
print ()

# Iniciando com a pergunta.
numero = int(input('Digite um número para descobrir \nse ele é par ou impar: '))
print ()

# Criando a condição.
if numero % 2 == 0:
    print ('O número {} é PAR.'.format(numero))
else:
    print ('O número {} é IMPAR.'.format(numero))

print ()
print ('='*43)