numero = int(input("Escolhe um numero pra tabuada até 10: "))
tabuada = [1,2,3,4,5,6,7,8,9,10]
for tab in range(len(tabuada)):
    tabuada[tab] = tabuada[tab] * numero
print(tabuada)