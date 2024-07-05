from random import randint
numero_s = randint(0, 100)
chute = int(input("Chute um numero ai filho. "))
tentativas = 0    

while chute != numero_s :
    if chute >= numero_s:
        print("o numero da sorte é menor.")
        chute = int(input("Tenta de novo maluco."))
        tentativas += 1
    elif chute <= numero_s:
        print("O numero da sorte é maior")
        chute = int(input("Tenta de novo maluco."))
        tentativas += 1
if chute == numero_s:
    print(f"Você acertou! O numero da sorte era {chute}. Você teve {tentativas} tentativas até acertar.")
