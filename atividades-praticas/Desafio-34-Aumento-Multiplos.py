'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00 ,calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
'''

# Desafio
print ()
print ('='*53)
print ('                      DESAFIO 34')
print ('='*53)
print ()

# Realizando a pergunta e armazenando dados.
salario = int(input('Qual o salário do funcionário R$ '))

# Criando o limite
limite = int(1250)
print ()

# Criando condição com fórmula
if salario > limite:
    salario = salario * 1.10 # Cento e dez porcento.
    print ('Seu novo salário com reajuste R$ {:.2f}'.format(salario))
else:
    salario = salario * 1.15
    print ('Seu novo salário com reajuste R$ {:.2f}'.format(salario))
print ()
print ('='*53)

