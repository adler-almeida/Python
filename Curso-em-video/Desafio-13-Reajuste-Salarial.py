#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print ()
print ('================================================================')
print ('                           DESAFIO  13                          ')
print ('================================================================')
print ('Faça um algoritmo que leia o salário de um funcionário e \nmostre seu novo salário, com a % de aumento. ')
print ('================================================================')
print ()

print()
nome = str(input('Informe o nome do colaborador: '))
salario = float(input('Informe o salário atual do colaborador {} R$ '.format(nome)))
aumporcento = int(input('Informe quantos porcento de aumento: % '))


cemporcento = int(100)
realporcento = cemporcento + aumporcento
fator = realporcento / cemporcento
novovalor = fator * salario

print ()
print ('================================================================')
print ()
print ('Salário anterior do colaborador {} , R$ {:.2f}'.format(nome,salario))
print ('Novo valor com {}% de aumento: R$ {:.2f}'.format(aumporcento,novovalor))
print ()
print ('================================================================')