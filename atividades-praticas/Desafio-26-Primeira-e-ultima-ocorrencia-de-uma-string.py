"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
"""

print ()
print ('='*53)
print ('                    DESAFIO 26')
print ('='*53)
print ()

# Salvando a frase e tornando maiuscula.
frase = str(input('Escreva uma frase: '))
frase = frase.upper ().replace(" ","")

# Contando quantas vezes aparece a letra 'A'.
print ()
print ('A letra "a" aparece {} vezes.'.format(frase.count('A')))
print ('A letra "a" aparece a primeira vez na posição {}'.format(frase.find('A')))
print ('A letra "a" aparece a ultima vez na posição {}'.format(frase.rfind('A')))
print ()
print ('='*53)

