#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print ('======== DESAFIO 007 ========')
print ()
print ('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.')
print ()
print ('=============================')
print ()

aluno = input('Informe o nome do Aluno: ')
nota1 = float(input('Informe a primeira nota: '))  #aqui não é stringe, por isso identifiquei como int de inteiro
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

print()
print ('=============================')
print ('A media do Aluno {} é {:.1f}'.format(aluno,media))
print ('=============================')