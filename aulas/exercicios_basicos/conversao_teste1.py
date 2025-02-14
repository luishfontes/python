numero = input('Digite um número: \n')
print('tipo atual do número:')
print(type(numero))

numero_convertido = int(numero)
print('novo tipo: ')
print(type(numero_convertido))

print(f'Seu número {numero_convertido}, foi convertido para inteiro')

# Nesse teste a idade não pode ser um caractere, apenas números inteiros.