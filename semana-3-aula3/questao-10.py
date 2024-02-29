#Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."
nome = str(input('Coloque seu nome:'))
spl = nome.split()
iniciais = spl[0][0:1]
iniciais1 = spl[1][0:1]
iniciais2 = spl[2][0:1]
iniciais3 = spl[3][0:1]
iniciais4 = spl[4][0:1]
print(iniciais, iniciais1,iniciais2, iniciais3, iniciais4)