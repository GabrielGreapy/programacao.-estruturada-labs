#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."
nome = str(input('Coloque seu nome:'))
spl = nome.split()
iniciais = spl[0][0:1]