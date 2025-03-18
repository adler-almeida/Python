#Faça um programa em python que abra e reproduza o áudio de um arquivo Mp3.

import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo mp3, arquivo salvo no mesmo diretório do desafio.
pygame.mixer.music.load('harry-potter.mp3')

# Reproduzir a música
pygame.mixer.music.play()

# Manter o programa executando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

"""
Resumo da Atividade: Tocar Música MP3 com Pygame
Importação e Inicialização: O módulo pygame é importado e o mixer é inicializado para lidar com o som.

Carregar e Reproduzir Música: A música é carregada utilizando pygame.mixer.music.load() e começa a tocar com pygame.mixer.music.play().

Controle de Execução: O loop while pygame.mixer.music.get_busy() mantém o programa ativo enquanto a música toca, com pygame.time.Clock().tick(10) garantindo a execução eficiente.
"""