#Verificação de Ano Bissexto: Escreva um programa que verifica se um ano fornecido pelo usuário é bissexto ou não.
ano = int(input('Selecione o ano: '))
if (ano % 4 ) == 0 : 
    print('É bisexto :0')
elif (ano % 100) == 0:
    print('Não é bisexto')
elif (ano % 400) == 0 :
    print('É bisexto')
