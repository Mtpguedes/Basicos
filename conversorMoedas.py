import math as m

print('Seja bem vindo ao conversor de moedas')

moeda = input('Para qual moeda você deseja a conversão? ')

cotacao = float(input(f'Qual a cotação atual do(a) {moeda}? '))

valor = float(input('Quanto você deseja converter? '))

if cotacao < 1:
    conversao = m.ceil(valor/cotacao)
else:
    conversao = m.ceil(valor*cotacao)

print(f'Dada a cotação atual de {cotacao} do {moeda} e o valor desejado de {valor}, São necessários {conversao} na sua moeda para obter o valor desejado.')