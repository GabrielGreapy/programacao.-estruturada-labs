#Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@").
email = input('Coloque seu e-mail')
arouba = email.find('@')

print(email[:arouba], email[arouba + 1:-1])