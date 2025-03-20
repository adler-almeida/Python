"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas.
- O nome com todas minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

"""

print ()
print ('='*63)
print ('                          DESAFIO 22')
print ('='*63)
print ()

nomec = str(input('Informe seu nome completo: '))

print ()
print ('Seu nome completo em letras maiúsculas: {}'.format(nomec.upper()))
print ('Seu nome completo em letras minúsculas: {}'.format(nomec.lower()))
print ('Espaços ao todo: {}'.format(len(nomec)))
print ('Seu nome completo possui: {} letras'.format(len(nomec.replace(" ", ""))))
#divisão da str nomec
dividir = nomec.split()
print ('Seu primeiro nome possui {} letras'.format(len(dividir[0])))
print ()
print ('='*63)


