'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 045 para viagens mais longas.
'''

# Desafio
print ()
print ('='*53)
print ('                      DESAFIO 31')
print ('='*53)
print ()

# Realizando a pergunta e armazenando dado.
print ('Olá, vamos calcular o preço da passagem')
km = int(input('Para isso, informe quantos km é sua distância.: '))
print ()

# Armazenando o limite de km solicitado
limite = int(200)

# Realizando condição com a formúla para cada ocasião.
if km > limite:
    km = km * 0.45
    print ('O preço da passagem a pagar será R${:.2f}.'.format(km))
else:
    km = km * 0.50
    print ('O preço da passagem a pagar será R${:.2f}.'.format(km))

print ()
print ('='*53)
