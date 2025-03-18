print ('==== OPERAÇOES ARITMETICAS ====')

# ** potência, exemplo 5²
# // Divisão inteiro, ex: 5/2= 2 inteiros
# % Resto da divisão, ex. 5/2= 1 de resto.
# == igual em operação aritmética se usa-se (2 ==)

# Ordem de precedência
# 1º  ()
# 2º  **
# 3º  * , / , // , %
# 4º  + , -


numero1 = int(input('Um valor: '))
numero2 = int(input('Outro valor: '))


print()
somar = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisaointeiro = numero1 // numero2
expoenciacao = numero1 ** numero2

#para dizer quantas casas apos a virgula, :.nf de flutuante, para pegar as 3 casas após a virgula, e n, significa numero.

print('A soma é {}, o produto é {} e a divisão {:.3f}'.format(somar, multiplicacao,divisao)) #.format no final é para fazer uma chamada a algum objeto, e no parenteses ele é informado.
print ()
print('Divisao de Inteiros é {} e potência {}'.format(divisaointeiro, expoenciacao))

# ,end = ' ' caso queira que tudo fique na mesma linha.
# \n linha nova