#len() Retorna o tamanho da minha lista.
# Iterar é percorrer cada um dos elementos

'''idades = [3, 5, 27, 1, 2, 45, 60, 6 ,1.5]

for i in range(0, len(idades)): #Nesse caso eu usei o len(idades) pra pegar logo o número total de elementos da minha lista
    print(idades[i])
# Essa é uma forma de ser feita, mas não é a aconselhada.

idades = [3, 5, 27, 1, 2, 45, 60, 6 ,1.5] #essa é a forma "pythonica" de exibir uma iteração.

for i in idades:
    print(i)

# Para acessar o valor e o index, podemos usar o enumerate()
# ele vai mostrando e enumerando.
idades = [3, 5, 27, 1, 2, 45, 60, 6 ,1.5]

x = list(enumerate(idades))

print(x)

# Aqui a gente tá fazendo i ter a posição e j ter os valores da lista

idades = [3, 5, 27, 1, 2, 45, 60, 6 ,1.5]

for i,j in enumerate(idades):
    print(f'i = {i} j = {j}')

idades = [3, 5, 27, 1, 2, 45, 60, 6 ,1.5]

idades_pares = []

for i in idades:
    if i % 2 ==0:
        idades_pares.append(i)

print(idades_pares)'''

idades = [[1, 2, 3, 4, 5], [6, 7, 8, 9 ,10], [11, 12, 13, 14, 15]]

for i in range(0, len(idades)):
    for j in range(0, len(idades[i])):
        print(idades[i][j])

# Pode parecer confuso.
# o código tá funcionando como o da tabuada, só que com listas.
# o i é a linha e o j é a coluna e o código tá percorrendo sos dois
# e como len(idades) é o total de elementos (nesse caso as listas), vamos do 0 até o total
# mas pq eu usei len(idades[i]) no for j?
# o i é o número inteiro nesse caso, ele n possui a propriedade i, então fazemos len(idades[i])
# idades na posição i, vale o len dessa lista.
# o len(idades) é 3, o len(idades[i]) é 5
# então para exibir cada um dos elementos da lista, deve ser feito esse código de cima.
# print(idades([i][j])), vai exibir os valores.
# ex: print(idades([0][0])), nesse código iria retornar o valor da primeira linha da primeira coluna
# ia exibir o valor 1. e assim por diante.