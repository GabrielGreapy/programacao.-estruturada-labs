lista = [i**2 for i in range(1, 11)]
print(lista)
lista2 = map(lambda x: x*2 if x > 5 else x, lista)     