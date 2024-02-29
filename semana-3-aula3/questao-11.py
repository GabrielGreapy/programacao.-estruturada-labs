#Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. Por exemplo: "O total de segundos é {total_segundos}."
hora = int(input('Quantidade de horas'))
minuto = int(input('Quantidade de minuto'))
segundos = int(input('Quantidade de segundos'))
fin = (hora * 3600) + (minuto * 60) + segundos
print('A quantidade de segundos é {} segundos.'.format(fin) )