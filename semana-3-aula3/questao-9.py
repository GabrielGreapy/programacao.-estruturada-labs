#Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). Em seguida, imprima a frase formatada.
frase = input('Digite a frase:')
frase_nova = frase.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
print(frase_nova)
