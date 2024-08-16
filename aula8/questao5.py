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