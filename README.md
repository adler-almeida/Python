# 📌 Repositório de Estudos em Python

Este repositório contém atividades, exercícios e anotações sobre a linguagem Python. Ele serve como um histórico de evolução e aprendizado, sendo uma referência para futuras consultas.

### 🔍 Sobre o Repositório
- Exercícios e projetos práticos realizados durante meus estudos.
- Anotações sobre conceitos e comandos importantes.
- Atualizações constantes conforme avanço nos estudos.

## 📚 Conceitos e Comandos
### Tipos de Dados
```python
# Imprimir na tela
print("Hello, World!")

# Entrada de dados
input("Digite algo: ")

# Tipos de variáveis
int_var = 10      # Inteiro
float_var = 7.0   # Números reais (flutuantes)
bool_var = True   # Valores lógicos (True ou False)
str_var = "Ola"   # Texto (strings)
````
## 🧮 Operações Aritméticas
````python
# ** Potência
resultado = 5 ** 2  # 25

# // Divisão inteira
resultado = 5 // 2  # 2

# % Resto da divisão
resultado = 5 % 2   # 1

# == Igualdade
comparacao = (2 == 2)  # True
````
## 📌 Ordem de Precedência
```python
1º: () Parênteses
2º: ** Potência
3º: *, /, //, % Multiplicação, Divisão, Divisão inteira e Resto
4º: +, - Soma e Subtração
```

## 🧑‍💻 Bibliotecas Importantes
### 📐 Módulo math
O módulo math contém funções matemáticas, como cálculos de raízes quadradas, trigonometria e mais.
import math
```python
import math

# Raiz quadrada
print(math.sqrt(16))  # 4.0
```
### 🎶 Módulo pygame (Música)
O pygame pode ser utilizado para tocar arquivos de áudio, como músicas em formato MP3.
```python
import pygame

# Inicializa o Pygame
pygame.init()

# Carrega e toca uma música
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()

# Aguarda a música terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
```
## 🚀 Como Utilizar
Para usar os arquivos deste repositório, siga os passos abaixo:

1️⃣ Baixar o Repositório
Se você deseja apenas visualizar os arquivos, pode acessar diretamente pelo GitHub. Mas se quiser rodar os códigos no seu computador, siga este passo:

- Se você tem Git instalado, pode clonar o repositório com este comando:
```markdown
git clone https://github.com/adler-almeida/Python.git
```
- Caso não tenha Git, basta clicar no botão Code e depois em Download ZIP. Extraia o arquivo no seu computador.

2️⃣ Acessar a Pasta do Projeto
Abra o terminal (ou prompt de comando) e entre na pasta do projeto:
```markdown
cd Python
```
3️⃣ Executar um Arquivo Python
Para rodar um arquivo Python, use o comando:
```markdown
python3 nome_do_arquivo.py
```
Substitua nome_do_arquivo.py pelo arquivo que deseja executar.

📌 Dica: Se você não tem o Python instalado, baixe-o no site oficial: python.org

## 🔄 Atualizações Futuras

- Adicionar mais conceitos e anotações conforme avanço nos estudos.
- Criar scripts práticos e desafios para reforçar o aprendizado.

📌 Mantenha-se atualizado! Este repositório será expandido constantemente com novos conteúdos.

📌 Sugestões são bem-vindas! Se você tem alguma dica ou melhoria, sinta-se à vontade para contribuir. 😃
