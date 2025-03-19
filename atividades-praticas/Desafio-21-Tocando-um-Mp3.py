# Faça um programa em python que abra e reproduza o áudio de um arquivo Mp3.
# **Importando modulo**

import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo mp3, arquivo salvo no mesmo diretório do desafio.
pygame.mixer.music.load('Harry-Potter.mp3')

# Reproduzir a música
pygame.mixer.music.play()

# Manter o programa executando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

"""
Resumo do Desafio: Tocar Música MP3 com Pygame

1º Importação e Inicialização:
   - O módulo pygame é importado.
   - O pygame.mixer é inicializado para trabalhar com som.
   
2 º Carregar e Reproduzir Música:
   - A música é carregada com pygame.mixer.music.load().
   - A reprodução é iniciada com pygame.mixer.music.play().
   
3º Controle de Execução:
   - O loop while pygame.mixer.music.get_busy() mantém o programa ativo enquanto a música toca.
   - pygame.time.Clock().tick(10) controla a taxa de execução do loop.
"""