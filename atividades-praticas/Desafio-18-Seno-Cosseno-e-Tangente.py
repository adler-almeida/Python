"""
Faça um programa que leia um Ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
**Importando Módulo**
"""

#importar modulo de matematica.
import math

print ()
print ('='*43)
print ('                  DESAFIO 18')
print ('='*43)
print ()

graus = float(input('Informe um angulo qualquer em graus: '))
print ()

#para esse desafio, precisa-se converter angulo em radiano para realizar o calculo no python, importando o modulo fazendo chamada.
radiano = math.radians(graus)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

#agora informar na tela.
print ('Seno de {}º: {:.3f}.'.format(graus,seno))
print ('Cosseno de {}º: {:.3f}.'.format(graus,cosseno))
print ('Tangente de {}º: {:.3f}.'.format(graus,tangente))
print ()
print ('='*43)
