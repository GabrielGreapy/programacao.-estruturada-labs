numero = int(input("Digite um numero positivo, senão... "))
numeros = 0
contador = 0
while numero > 0 :
    numeros += numero
    numero = int(input("Digite mais outro numero positivo..."))
    contador += 1
print(f'A soma dos numeros positivos que você criou é {numeros}, você digitou {contador} numeros e o seu ultimo numero digitado foi {numero}')


