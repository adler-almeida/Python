#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

print ()
print ('============= DESAFIO 05  AULA 07 =============')
print ('Faça um programa que leia um número inteiro \ne mostre na tela seu sucessor e seu antecessor.')
print ('================================================')

print ()
numero = int(input('Digite um número: '))

sucessor = numero + 1
antecessor = numero - 1

print ()
print ('================================================')
print ('Sucessor de {} é {}'.format(numero, sucessor))
print ('Antecessor de {} é {}'.format(numero,antecessor))
print ('================================================')
