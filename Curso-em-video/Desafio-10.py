#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólaree ela pode comprar. Considere US $ 1,00 = R$ 3,27

print ('================ DESAFIO 010 ================')
print ()
print ('Conversor de Real para Dólar.')
print ()
print ('=============================================')
print ()

valor = float(input('Informe o valor que possui na carteira R$ '))
dolar = float(3.27)
conversor = valor / dolar
print ()

print ('Você poderá trocar R${:.2f} por U${:.2f} dólares.'.format(valor,conversor))

