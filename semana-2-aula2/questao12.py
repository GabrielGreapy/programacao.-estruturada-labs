#Escreva um programa que solicite ao usuário a sua idade e verifique se ele é maior de idade (idade igual ou superior a 18 anos). Imprima uma mensagem informando o resultado.#
idade = int(input('Coloque sua idade aqui:'))
nome = str(input('Coloque seu nome aqui:'))
print("Seu nome é:",nome)
if idade <= 18 : print("Sua idade é",idade,"e você é menor de idade")
else: print("Sua idade é",idade,"e você é maior de idade")