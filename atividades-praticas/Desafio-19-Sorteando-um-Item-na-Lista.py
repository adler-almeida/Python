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

#agora realizar o sorteio aleatorio de uma str.
sorteado = random.choice([aluno1,aluno2,aluno3,aluno4])
print ('O Aluno sorteado para realizar a tarefa de apagar o quadro será {}.'.format(sorteado))
print ()
print ('='*43)