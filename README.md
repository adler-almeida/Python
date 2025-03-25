# 📝 Repositório de Estudos em Python

Este repositório contém atividades, exercícios e anotações sobre a linguagem Python. Ele serve como um histórico de evolução e aprendizado, sendo uma referência para futuras consultas.

---

## 🔍 Sobre o Repositório
- 📂 Exercícios e projetos práticos realizados durante meus estudos.
- 📖 Anotações sobre conceitos e comandos importantes.
- 🔄 Atualizações constantes conforme avanço nos estudos.

---

## 📚 Conceitos e Comandos

### 📌 Tipos de Dados
```python
# Imprimir na tela
print("Hello, World!")

# Entrada de dados
input("Digite algo: ")

# Tipos de variáveis
int_var = 10      # Inteiro
float_var = 7.0   # Números reais (flutuantes)
bool_var = True   # Valores lógicos (True ou False)
str_var = "Olá"   # Texto (strings)
```

### 🧮 Operações Aritméticas
```python
# ** Potência
resultado = 5 ** 2  # 25

# // Divisão inteira
resultado = 5 // 2  # 2

# % Resto da divisão
resultado = 5 % 2   # 1

# == Igualdade
comparacao = (2 == 2)  # True
```

### 📌 Ordem de Precedência
```python
1º: () Parênteses
2º: ** Potência
3º: *, /, //, % Multiplicação, Divisão, Divisão inteira e Resto
4º: +, - Soma e Subtração
```

---
## 🔄 Condicionais: if e else
O if e else são usados para tomar decisões em seu código. O Python executa um bloco de código se uma condição for verdadeira, e outro bloco se for falsa.
### Exemplo de uso:
````python
idade = 18

# Se a idade for maior ou igual a 18, é maior de idade, senão é menor de idade
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
````
### Explicação:
- **if**: Executa o código dentro do bloco se a condição for verdadeira.
- **else**: Executa o código dentro do bloco se a condição do if for falsa.

### Exemplo com elif:
O **elif** é utilizado quando queremos verificar múltiplas condições.
````python
nota = 8

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
````
---
## 🧑‍💻 Bibliotecas Importantes

### 📐 Módulo math
O módulo `math` contém funções matemáticas, como cálculos de raízes quadradas, trigonometria e mais.
```python
import math

# Raiz quadrada
print(math.sqrt(16))  # 4.0
```

### 🎶 Módulo pygame (Música)
O `pygame` pode ser utilizado para tocar arquivos de áudio, como músicas em formato MP3.
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

---

## 🔤 Análise e Manipulação de Strings

### 📏 Análise
```python
# len() - Conta o número de caracteres
len(frase)

# count() - Conta quantas vezes um caractere aparece
frase.count('o')
frase.count('o', 0, 13)  # Conta de 0 a 12 (última posição ignorada)

# find() - Retorna a posição onde a substring começa
frase.find('deo')  # Se não encontrar, retorna -1

# in - Verifica se uma string está dentro de outra
frutas = ["maçã", "banana", "uva"]
print("banana" in frutas)  # True
print("melancia" in frutas)  # False
```

### 🔄 Transformação
```python
# replace() - Substitui trechos de uma string
frase.replace("banana", "melancia")

# upper() - Converte para maiúsculas
txt.upper()

# lower() - Converte para minúsculas
txt.lower()

# capitalize() - Primeira letra maiúscula, resto minúsculo
txt.capitalize()

# title() - Primeira letra de cada palavra maiúscula
txt.title()

# strip() - Remove espaços no início e no fim
txt.strip()

# rstrip() - Remove espaços à direita
txt.rstrip()

# lstrip() - Remove espaços à esquerda
txt.lstrip()
```

### ✂️ Divisão e Junção
```python
# split() - Divide a string em uma lista
frase.split()

# join() - Junta elementos de uma lista em uma string
"-".join(frase)  # Adiciona "-" entre os elementos
```

### 🎯 Exemplos
```python
frase = 'Curso em Vídeo Python'
       # 0123456789...........

print(frase[3])  # 's'
print(frase[3:13])  # 'so em Víde'
print(frase[:13:2])  # 'Cro íe'
print(frase.upper().count('O'))  # 3
print(frase.replace('Python', 'Android'))  # 'Curso em Vídeo Android'

# Divisão e acesso a partes da string
dividido = frase.split()
print(dividido[2][4])  # 'o'
```

---

## 🚀 Como Utilizar

### 1️⃣ Baixar o Repositório
Se você deseja apenas visualizar os arquivos, pode acessar diretamente pelo GitHub. Mas se quiser rodar os códigos no seu computador, siga este passo:

- Se você tem Git instalado, pode clonar o repositório com este comando:
```sh
git clone https://github.com/adler-almeida/Python.git
```
- Caso não tenha Git, basta clicar no botão `Code` e depois em `Download ZIP`. Extraia o arquivo no seu computador.

### 2️⃣ Acessar a Pasta do Projeto
Abra o terminal (ou prompt de comando) e entre na pasta do projeto:
```sh
cd Python
```

### 3️⃣ Executar um Arquivo Python
Para rodar um arquivo Python, use o comando:
```sh
python3 nome_do_arquivo.py
```
Substitua `nome_do_arquivo.py` pelo arquivo que deseja executar.

📌 **Dica:** Se você não tem o Python instalado, baixe-o no site oficial: [python.org](https://www.python.org/)

---

## 🔄 Atualizações Futuras

- 📌 Adicionar mais conceitos e anotações conforme avanço nos estudos.
- 🔧 Criar scripts práticos e desafios para reforçar o aprendizado.
- 🚀 Explorar mais bibliotecas úteis para desenvolvimento.

📌 **Mantenha-se atualizado!** Este repositório será expandido constantemente com novos conteúdos.

📌 **Sugestões são bem-vindas!** Se você tem alguma dica ou melhoria, sinta-se à vontade para contribuir. 😃
