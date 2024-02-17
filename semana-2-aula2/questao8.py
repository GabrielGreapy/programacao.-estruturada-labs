#Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado.#
num = int(input("Verifique se o seu numero é par ou impar "))
resultado = (num) % 2
if resultado == 0 : print(num, ' é par.')
else: print(num, 'É impar.')
