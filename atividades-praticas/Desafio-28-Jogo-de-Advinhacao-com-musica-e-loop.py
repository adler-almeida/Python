'''
Escreva um programa que faça o computadr "pensar" em um número interio entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O Programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
import pygame
import os

# Inicializar o mixer
pygame.init()
# Carregar o arquivo e reproduz em loop abaixo.
pygame.mixer.music.load('Harry-Potter.mp3')
pygame.mixer.music.play(-1)

# Loop principal
while True:
    # Limpa a tela antes de repetir
    os.system("cls" if os.name == "nt" else "clear") # Windows ou linux.

# Tela
    print ()
    print ('='*43)
    print ('                  DESAFIO 28')
    print ('='*43)
    print ()
    print ('Deixe-me pensar em número')
    print ()
    print ('Pensando...')
    print ()

# Escolhendo e armazenando um número
    nsorteado = random.randint(0,5)
    print ('Já escolhi um número! Agora é sua vez.')
    print ('Voce deverá escolher um número de 0 a 5')
    print ()
    ninformado = int(input('Qual número você informa? '))

# Criando condição para 2 possiveis caminhos, se acertar ou não.
    if ninformado == nsorteado:
        print ('Parabéns, você conseguiu acertar!')
    else:
        print ('Infelizmente você não acertou.')
        print ('Eu escolhi o número {}.'.format(nsorteado))

# Finalizando a música com condição
    print ()
    pergunta = str(input("Digite 'sair' para encerrar ou 'sim' para continuar: "))
    if pergunta.lower().replace(" ","") == "sim":
        print ('O programa será repetido...')
    else:
        print ('Saindo do programa...')
        break  # sai do loop se o usuário digitar sair

pygame.quit() # encerrar o pygame quando o usuario digitar sair