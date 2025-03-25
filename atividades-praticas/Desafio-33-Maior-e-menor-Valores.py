'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

# Desafio
print ()
print ('='*53)
print ('                      DESAFIO 33')
print ('='*53)
print ()

# Enunciado
print ('Informe três números, que irei lhe dizer \nqual é o menor e o maior')
print ()

# Coletando dados.
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))

# Criando lista
lista = [numero1,numero2,numero3]

'''
# Organizando lista do menor para o maior
lista.sort()

# Exibir na tela o menor e maior valor através da análise
print (f'Menor valor digitado {lista[0]}') # f de string
print (f'Maior valor digitado {lista[2]}')
'''
# Organizar lista do menor para o maior
lista.sort()

# Valor minimo e máximo.
menorvalor = min(lista)
maiorvalor = max(lista)

# Exibir na tela o menor e maior valor
print ()
print (f'Menor valor digitado {menorvalor}') # f de string
print (f'Maior valor digitado {maiorvalor}')
print ()
print ('='*53)