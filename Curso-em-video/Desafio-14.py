#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

print ()
print ('============================================')
print ('                 DESAFIO 14')
print ('='*44)
print ('          Conversor de ºC para ºF')
print ('='*44)

print ()
celsius = float(input('Favor informar a temperatura em Cº: '))

fahrenheit = float(celsius*1.8)+32

print ()
print ('{} ºC equivale a {:.2f} ºF'.format(celsius,fahrenheit))

print ()
print ('='*44)
print ('- C é a temperatura em Celsius {} ºC'.format(celsius))
print ('- F é a temperatura em Fahrenheit {:.2f} ºF'.format(fahrenheit))
print ('='*44)