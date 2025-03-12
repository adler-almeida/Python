#Faça um programa que leia a largura e a altura de uma parede em metros,
#Calcule a sua área e a quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta, pinta uma área de 2m².

print ()
print ('================ DESAFIO 011 ================')
print ()
print ('Quantos litros serão necessários para pintar \numa determinada parede')
print ()
print ('=============================================')
print ()

altura = float(input('Informe a Altura da Parede: '))
largura = float(input('Informe a Largura da Parede: '))

area = altura * largura

litros = area / 2

print ()
print ('Area total da parede: {}m² \nSerão necessários {} litros de tinta.'.format(area,litros))
