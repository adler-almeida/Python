#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.

print ()
print ('=============================================')
print ('                 DESAFIO 15')
print ('='*45)
print ('    Calcule o preço a pagar, sabendo que \n    o carro custa R$ 60,00 por dia e \n    R$ 0,15 por Km rodado.')
print ('='*45)

km = float(input('Quantos Kilometros percorreu com o carro? '))
dias = int(input('Quantos dias o carro foi alugado? '))

apagar = float(km*0.15)+(60*dias)

print ()
print ('='*45)
print ('O valor a ser pago ao total: R$ {:.2f}'.format(apagar))
print ('='*45)

