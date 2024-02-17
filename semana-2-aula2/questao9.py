#Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.#
perg1 = str(input('Você está logado?'))
if(perg1 == 'sim'): perg1 = True
if(perg1 == 'nao'): perg1 = False
perg2 = str(input('Serviços disponiveis?'))
if(perg2 == 'sim'): perg2 = True
if(perg2 == 'nao'): perg2 = False


if (perg1 and perg2) == True: print("Você está logado e pronto para utilizar o serviço.")
if not (perg1 and perg2) == True: print('Você não está logado ou com serviços disponiveis.')
if (perg1 or perg2) == False: print('Uma de suas respostas está incorreta.')