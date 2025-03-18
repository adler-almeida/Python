"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
ele, lendo o nome deles e escrevendo o nome escolhido.
"""
import random

print ()
print ('='*43)
print ('                  DESAFIO 19')
print ('='*43)
print ()

#receber nome de alunos
aluno1 = str(input('Favor informar o nome do 1º aluno: '))
aluno2 = str(input('Favor informar o nome do 2º aluno: '))
aluno3 = str(input('Favor informar o nome do 3º aluno: '))
aluno4 = str(input('Favor informar o nome do 4º aluno: '))
print ()

#criando a lista de alunos
alunos = [aluno1,aluno2,aluno3,aluno4]

#escolhendo um aluno aleatório
sorteado = random.choice(alunos)

#exibir na tela
print ('O Aluno sorteado para realizar a tarefa \nde apagar o quadro será {}.'.format(sorteado))
print ()
print ('='*43)

"""
Se quiser um único nome aleatório, use random.choice(). Se quiser misturar e exibir todos na nova ordem, use random.shuffle().
"""