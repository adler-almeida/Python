"""
## Analise de String:

### len
len(frase) / len = ler.

### count
frase.count('o') / count = contar
frase.count('o',0,13) / count = contar, ex citado, irá contar 0 a 12, sempre ignorando a ultima casa, que seria o 13.

### find
frase.find('deo') / find = encontrar, ele conta e diz em que posição começa as palavras "deo"

### in
frutas = ["maçã", "banana", "uva"]  / frutas receberá essa lista [].

print("banana" in frutas)  # True / in = dentro, dentro de frutas, tem banana? true = verdadeiro.
print("melancia" in frutas)  # False / in = dentro, dentro de frutas, tem melancia? false = falso.

## Transformação:

### replace
frutas.replace ('banana','melancia') # replace = substituir, trocar. localizar e trocar banana por melancia.

### upper
frase.upper () # upper = para cima, superior, ele torna as letras menores em MAIORES, maiúsculas.

### lower
frase.lower () # lower = mais baixo, ele torna as letras MAIORES em menores, minúsculas.

### capitalize
frase.capitalize () # capitalize, ele vai tornar as letras MAIORES em menores, * exceto a string da casa 0.

### title
frase.title () # title, ele localiza todas as primeiras das Strings e as transformam em MAIORES, maiúsculas, somente as primeiras que estão separadas por espaço e 0.
o restante fica em minúsculo.

### strip
frase.strip () # strip = tira, ele tira da string espaçõs vazios do inicio e fim.

### rstrip
frase.rstrip () # r de right = direita, remove somente os espaços vazios da direita, que fica localizado no final da frase o restante se mantém.

### lstrip
frase.lstrip () # l de left = esquerda, remove somente os espaços vazios da esquerda, que fica localizado no inicio da frase o restante se mantém.

## Divisão
### split
frase.split () # split = dividir, ele separa todas as palavras eliminando os espaços vazios, do inicio ao fim, e considera cada str como única, ou seja,
cada str que tinha espaço agora n tem mas, passa a iniciar com 0, sendo 1..n de uma lista.

## Junção
### join
'-'.join(frase) # ele coloca (-) traço, em todos os espaços vazios da string, ou se você preferir espaços em branco, é só substituir por espaço em branco.


** -1 singnifica que NÃO foi encontrado. **
"""

frase = 'Curso em Vídeo Python'
       # 0123456789...........
print(frase[3])
# s

print ()
print (frase[3:13]) # de numero x até o numero informado y, ele sempre ira considerar y-1.
# so em Víde

print ()
print (frase[:13:2]) # irá comerçar pelo 0, pois não foi informado, e vai ir até a casa 13-1=12, e pular de 2 em 2 e informar.
# Croe íe

print ()
print (frase.upper().count('O')) # Irá jogar tudo para CIMA e contar os 'O's.
# 3

print ()
print (frase.replace('python','Android'))
# Curso em Vídeo Python

print ()
dividido = frase.split ()
print (dividido[2][4]) # mostrar dentro do 2 grupo da frase o 4 caractere.
# o
