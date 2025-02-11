#Receba 10 valores e exiba a soma de todos eles

v = [int(input('Digite um valor; '))for i in range(0, 5)]
#print(sum(v))

soma = 0
for i in v:
    print(f'Valor atual da soma entre {soma} + {i} = {soma + i}')
    soma = soma + i

print(f'Resultado = {soma}')