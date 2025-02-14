print('Identificador de números impares até o número que você escolher.')
valor = input('Digite até que número você quer saber os números impares: ')

if valor.isdigit():
    valor_int = int(valor)
    for numero in range(1, valor_int + 1):
        if numero %2 != 0:
            print(numero, end=' ')
else:
    print('Valor inválido.')