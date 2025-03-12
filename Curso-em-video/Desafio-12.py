#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print ()
print ('================ DESAFIO 012 ================')
print ()
print ('leia o preço de um produto e mostre seu novo\npreço, com % de desconto que você escolher.') #porém criei um que você adiciona o valor do desconto sobre o valor.
print ()
print ('=============================================')

print ()
desconto = int(input('Informe a % de desconto: '))
produto = float(input('Informe o valor do produto: R$ '))

porctotal = int(100)

porcreal = porctotal - desconto
fator = porcreal / porctotal
valorcomdesconto = fator * produto

print ()
print ('O valor do produto com {}% de desconto aplicado é R$ {:.2f}.'.format(desconto,valorcomdesconto))
print ()
print ('=============================================')
