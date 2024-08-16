# Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150.
def idade_valida(idade):
    if idade <= 150 and idade >= 0:
        if (idade / 1) == idade: 
            print('inteiro')
        else: 
            print('inteiro entre 0 a 150')
    else:
        print('fora de escopo')
idade = float(input(''))
idade_valida(idade)
    