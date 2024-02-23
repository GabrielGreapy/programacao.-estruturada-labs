#Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".
plv = str(input('Verifique se a palavra é um Palíndromo: '))
plv0 = plv.lower()
plv1 = plv0[::-1]
if plv == plv1: print('A palavra é um Palíndromos.')
else: print('As palavra não é um Palíndromo.') 