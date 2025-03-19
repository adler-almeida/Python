"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle

print ()
print ('='*43)
print ('                  DESAFIO 20')
print ('='*43)
print ()

#receber nome de alunos
aluno1 = str(input('Favor informar o nome do 1º aluno: '))
aluno2 = str(input('Favor informar o nome do 2º aluno: '))
aluno3 = str(input('Favor informar o nome do 3º aluno: '))
aluno4 = str(input('Favor informar o nome do 4º aluno: '))
print ()

#agora criar uma lista com os alunos e embaralhar..
lista = [aluno1,aluno2,aluno3,aluno4]   #lista precisa ser declarada em []

#embaralhar a lista
shuffle(lista)

print ('A ordem sorteada dos Alunos são: ')
print (lista)
print ('='*43)

"""
Se quiser um único nome aleatório, use random.choice(). Se quiser misturar e exibir todos na nova ordem, use random.shuffle().
"""