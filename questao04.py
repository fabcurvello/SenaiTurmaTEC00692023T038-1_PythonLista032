'''
4)	Desenvolver um programa que pergunte ao usuário o seu peso e sua altura.
Ao final o programa deverá exibir na tela o valor do índice de massa corporal
desta pessoa (IMC).
Fórmula:  IMC = peso / altura2  -  Obs: peso em quilos e altura em metros.
'''
import math

peso = float(input("Qual é o seu peso ?"))
altura = float(input("Qual a sua altura? "))

# Fórmula:  IMC = peso / altura2
# imc = peso / (altura * altura)
imc = peso / math.pow(altura, 2)

print(f"O seu IMC é {imc:.0f}")