'''
7)	A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações
sem juros. Faça um algoritmo que pergunte um valor de uma compra, o número
de prestações escolhidas e apresente como resultado o valor das prestações.
'''

valor_compra = float(input("Informe o valor total da compra: "))
num_prestacoes = float(input("Qual o número de prestações da compra? "))

valor_prestacao = valor_compra / num_prestacoes

print(f"O valor de cada uma das {num_prestacoes:.0f} prestações será de R$ {valor_prestacao:.2f}")
