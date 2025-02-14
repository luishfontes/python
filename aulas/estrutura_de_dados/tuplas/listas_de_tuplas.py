lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tuplas_lista = []

for i in range(0, len(lista), 2):
    tuplas_lista.append((lista[i], lista[i+1]))


print(tuplas_lista)