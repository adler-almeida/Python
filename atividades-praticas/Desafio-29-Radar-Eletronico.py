'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''
# Desafio
print ()
print ('='*43)
print ('                  DESAFIO 29')
print ('='*43)
print ()

limiteveloc = int(80)
velocinicial = int(input('Qual foi a velocidade percorrida? '))

print ()
if velocinicial > limiteveloc:
    velocinicial = (velocinicial - limiteveloc)* 7 # cada km ultrapassado *(vezes) o valor a pagar.
    print ('Sua multa será de R${:.2f}.'.format(velocinicial))
else:
    print ('Nenhum dividendo.')
print ()
print ('='*43)
