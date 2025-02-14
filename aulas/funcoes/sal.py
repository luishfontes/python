def contar_caracteres(texto):
    return len(texto)

def encontrar_vogais(texto):
    VOGAIS = 'AEIOU'
    vogais_encontradas = [letra for letra in texto if letra in VOGAIS]
    return vogais_encontradas, len(vogais_encontradas)

def digitos_encontrados(texto):
    digitos_encontrados = [letra for letra in texto if letra.isdigit()]
    return digitos_encontrados, len(digitos_encontrados)

def main():
    print('Programa para realizar contagem de vogais em um texto.')
    texto = input('\nInsira um texto: ')

    digitos, total_digitos = digitos_encontrados(texto)
    caracteres = contar_caracteres(texto)
    vogais, total_vogais = encontrar_vogais(texto)

    if vogais:
        print(f'Vogais encontradas: {', '.join(vogais)}')
    else:
        print('Não foram encontradas vogais neste texto.')
    
    print(f'Numero de caracteres no texto: {caracteres}.')
    print(f'Numero de vogais no texto: {total_vogais}')
    print(f'Digitos encontrados: {digitos}.')


print('Contamos quantas vogais tem no seu texto!')
texto = input('Digite o texto: ')

vogais = encontrar_vogais(texto)
print(vogais)