# Receba um número e mostre a tabuada cmopleta dele usando o laço for.

'''n1 = int(input('Digite um número: '))

for i in range(0, 11):
    print(f'{n1} x {i} = {n1 * i}')'''

# Neste código eu faço exibir apenas a tabuadas com resultado par.
# Também posso fazer com os "pulos" e popr range(0, 11, 2)
'''n1 = int(input('Digite um número: '))

for i in range(0, 11):
    if (n1 * i) % 2 == 0:
        print(f'{n1} x {i} = {n1 * i}')'''

# Agora vou exibir todas as tabuadas do 1 até o 10.

for i in range(1, 11):
    print(f'============[TABUADA DO {i}]============')
    for j in range(1, 11):
        print(f'{i} x {j} == {i * j}')