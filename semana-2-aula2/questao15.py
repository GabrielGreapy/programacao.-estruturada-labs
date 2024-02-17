#Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch﻿ Time (o número de milessegundos desde 00:00 de 01 de Janeiro de 1970).
dia = int(input("Coloque o dia:"))
mes = int(input("Coloque o mês, em numero:"))
ano = int(input("Coloque o ano:"))
dataepoch = (1, 1, 1970)
data = (dia, mes, ano)
ano = (ano - 1970)
milisegundos = (dia * 86400) + (mes * 31536000) + (ano * 315360000)


print(milisegundos)
