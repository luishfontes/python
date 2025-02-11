#Receba um número do usuário e mostre a tabuada deste número.

n1 = int(input('Digite o número cujo deseja saber a tabuada: '))

i = 1

while i <= 10:
    print(f'{n1} * {i} = {n1 * i}')
    i = i + 1

