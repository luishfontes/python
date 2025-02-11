# Identificando vogais no texto e fazendo uma contagem.

texto = input('Digite algo: ')
VOGAIS = 'AEIOUaeiou' 

caracteres = len(texto)
total_vogais = 0
vogais_encontradas = []  # vai armazenar vogais encontradas na lista

for letra in texto:
    if letra in VOGAIS:
        vogais_encontradas.append(letra)  # Adicionando a vogal
        total_vogais += 1

if vogais_encontradas:
    print(f'Vogais encontradas: {", ".join(vogais_encontradas)}')  # Exibe elas separadas pela virgula
else:
    print('Nenhuma vogal encontrada.')

print(f'Número de caracteres no seu texto: {caracteres}')
print(f'O número de vogais: {total_vogais}')


'''
# Aqui só tô testando pra ver como seria uma consulta por números.

texto = input('Digite qualquer coisa, pode conter números ou letras: ')

for numero in texto:
    if numero.isdigit():
        print(numero, end='')
'''