"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
meu bairro contém santo, então fiz como bairro.
"""

print ()
print ('='*43)
print ('                  DESAFIO 24')
print ('='*43)
print ()

cidade = str(input('Informe o nome do seu Bairro: '))
print ()

# tornando todas maiúsculas e dividir as palavras
cidade = cidade.upper().split()

# criar a variavel contendo a palavra de comparação:
santo = 'SANTO'

# condição if = se else = senao
if cidade[0] == santo:
    print ('Parabéns, sua cidade começa com SANTO.')
else:
    print ('Infelizmente sua cidade não começa com SANTO.')
print ()
print ('='*43)