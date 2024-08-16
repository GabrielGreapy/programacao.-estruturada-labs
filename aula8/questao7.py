# Defina uma função chamada potencia que calcula a potência de um número elevado a uma potência especificada. Forneça uma documentação estendida que explique como usar a função e inclua exemplos de uso.
def potencia(num, pot):
    """ Função da potência
        Nela você podera escolher um numero e uma base para descobrir a poteênci
        DO NUMERO ELEVADO A BASE
    Args:
        num (Numero que será elevado.)
        pot (numero que irá elevar.)
    """
    if pot == True:
        resultado = num ** pot
        print(f'{resultado}')
    else:
        resultado = num ** 2
        print(resultado)
num1 = int(input(''))
pot1 = int(input(''))
potencia(num1, pot1)