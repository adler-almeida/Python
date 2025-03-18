print ('==== DISSECANDO VARIAVEL 04 ====')

print ()
algo = input ('Digite algo: ') #input = entrada, recebimento.
print ('O tipo primitivo desse valor é ', type(algo)) #type significa o valor primitivo da variavel
print ('Só tem espaços? ', algo.isspace())  #irá verificar se a palavra possui espaço
print ('É um número? ', algo.isnumeric())  #is numeric é um numero?
print ('É alfabético? ', algo.isalpha())
print ('É alfanumérico? ', algo.isalnum())
print ('Está em maiúsculas? ', algo.isupper())
print ('Está em minusculas? ', algo.islower())
print ('Está capitalizada? ', algo.istitle())
