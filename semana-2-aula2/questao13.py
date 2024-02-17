#Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.#
#Instruções:Solicite ao usuário o primeiro número inteiro e armazene-o em uma variável chamada numero1. Solicite ao usuário o segundo número inteiro e armazene-o em uma variável chamada numero2. Troque os valores das variáveis numero1 e numero2 utilizando atribuição múltipla. Imprima os valores atualizados das variáveis utilizando a função print().
#Digite o primeiro número inteiro: 10#
#Digite o segundo número inteiro: 5#
#Valores antes da troca: numero1 = 10, numero2 = 5#
#Valores depois da troca: numero1 = 5, numero2 = 10#
num1 = int(input("Digite dois numeros diferentes para que as variaveis sejam alternadas. Primeiro numero:"))
num2 = int(input("Agora segundo numero:"))
temp = num1
num1 = num2
num2 = temp
print(num1)
print(num2)