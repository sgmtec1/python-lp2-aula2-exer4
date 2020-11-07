'''
Faça um programa que simule um lançamento de dados. O programa deve sortear 10 números
aleátorios (de 1 a 6) e armazenar esses números em uma lista.
Na sequência, informe quantas vezes cada número foi sorteado.
Exemplo:
Suponha que a lista com os números sorteados seja: [3, 1, 5, 3, 5, 4, 5, 5, 3, 1] .
Para esta lista, o programa deve exibir:
Número 1 foi sorteado 2 vezes
Número 2 foi sorteado 0 vezes
Número 3 foi sorteado 3 vezes
Número 4 foi sorteado 1 vezes
Número 5 foi sorteado 4 vezes
Número 6 foi sorteado 0 vezes]
'''

from random import randint

dados = []
for i in range(10):
    dados.append(randint(1, 6))

print('Números sorteados: ', dados)

for i in range(1,7):
    print('Número', i, 'foi sorteado', dados.count(i), 'vezes')

