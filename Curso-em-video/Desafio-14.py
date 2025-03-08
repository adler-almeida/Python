#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

print ()
print ('============================================')
print ('                 DESAFIO 14                 ')
print ('='*43)
print ()

celsius = float(input('Favor informar a temperatura em Cº: '))

fahrenheit = float(celsius*1.8)+32

print ()
print ('{:.1f} ºC equivale a {} ºF'.format(celsius,fahrenheit))

print ()
print ('='*43)
print ('- C é a temperatura em Celsius {} ºC'.format(celsius))
print ('- F é a temperatura em Fahrenheit {} ºF'.format(fahrenheit))
print ('='*43)