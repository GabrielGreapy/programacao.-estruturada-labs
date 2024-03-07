#Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas
frase = input('Digite uma frase')
if frase.isupper() == True: print('Todas as letras são caixa alta')
else: print('Todas as letras não são caixa alta')
