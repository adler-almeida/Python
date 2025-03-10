#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

print ('======== DESAFIO 008 ========')
print ()
print ('Escreva um programa que leia um valor em metros, e o exiba convertido em centimetros e milimetros.')
print ()
print ('=============================')
print ()

metros = float(input('Favor informar o valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print ('O valor informado é {}m., \nConvertido em {}cm. e {}mm.'.format(metros,centimetros,milimetros))
