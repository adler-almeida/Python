'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

print ()
print ('='*43)
print ('                  DESAFIO 23')
print ('='*43)
print ()

print ('Sistema de Numeração Decimal até Milhar')
numero = str(input('Informe um número: '))

# Preencher com 0 os campos vazios para evitar erro.
numero = numero.zfill(4) #zfill(4) preenche com zeros à esquerda,

# Criar as variaveis para armazenar cada informação e transmistir.
unidade = numero [-1]
dezenda = numero [-2]
centena = numero [-3]
milhar = numero [-4]
# A ideia dos índices negativos é contar de trás para frente da sequência, e -1 sempre será o último, -2 será o penúltimo, e assim por diante.

# Informar na tela
print ()
print ('Ordens:')
print ('Unidade: {}'.format(unidade))
print ('Dezenda: {}'.format(dezenda))
print ('Centena: {}'.format(centena))
print ('Milhar: {}'.format(milhar))
print ()
print ('='*43)