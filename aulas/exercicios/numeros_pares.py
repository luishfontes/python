# Receba um número e msotre todos os números pares de 0 até o número digitado.

print('Programa para exibir números pares.')
numero = int(input('Escolha seu número: '))

i = 0
while i <= numero:
    print(i, end=' ')
    if i%2 == 0:
        i += 2
