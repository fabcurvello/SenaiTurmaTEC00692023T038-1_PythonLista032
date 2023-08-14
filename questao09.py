'''
9)	Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
e mostre-a expressa apenas em dias. Obs: Considere os anos com 365 dias e os
meses com 30 dias.
'''

anos = int(input("Infome a sua idade (anos): "))
meses = int(input("Quantos meses completos já se passaram desde o seu último aniversário? "))
dias = int(input("Quantos dias se passaram após o número de meses completos da resposta anterior? "))

total_dias = (anos * 365) + (meses * 30) + dias

print("Você já viveu {} dias".format(total_dias))
